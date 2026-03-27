
import os
import sys
import asyncio
import logging
from pathlib import Path
from aiohttp import web

# Add deploy directory to Python path for imports
deploy_dir = Path(__file__).parent / 'deploy'
if deploy_dir.exists():
    sys.path.insert(0, str(deploy_dir))
else:
    print("Error: deploy directory not found")
    sys.exit(1)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger

# Health server for monitoring
async def health_check(request):
    """Health check endpoint"""
    return web.json_response({
        'status': 'healthy',
        'bot': 'TradeMaster AI',
        'version': '2.0'
    })

async def main():
    """Main entry point that runs TelegramHandler with health server"""
    try:
        # Import TelegramHandler from deploy folder
        from telegram_handler import TelegramHandler
        
        logger.info("=== Starting TradeMaster AI Bot ===")
        logger.info("Using full telegram_handler.py from deploy folder")
        
        # Create health server
        health_app = web.Application()
        health_app.router.add_get('/health', health_check)
        health_app.router.add_get('/', health_check)
        
        # Start health server
        runner = web.AppRunner(health_app)
        await runner.setup()
        site = web.TCPSite(runner, '0.0.0.0', 5000)
        await site.start()
        logger.info("✅ Health server started on port 5000")
        
        # Create and run the handler with all original services
        handler = TelegramHandler()
        
        logger.info("✅ TradeMaster AI Bot starting with full services...")
        
        # Start webhook monitor to prevent conflicts
        from webhook_monitor import start_webhook_monitor
        bot_token = os.getenv('TELEGRAM_API_TOKEN')
        monitor, monitor_task = await start_webhook_monitor(bot_token)
        logger.info("Webhook monitor started to prevent conflicts")
        
        # Run the bot with retry logic for webhook conflicts
        retry_count = 0
        max_retries = 3
        
        while retry_count < max_retries:
            try:
                # Force polling mode
                os.environ['TELEGRAM_POLLING_MODE'] = 'true'
                bot_task = asyncio.create_task(handler.run(use_webhook=False))
                await bot_task
                break  # Exit loop if successful
            except Exception as e:
                if "terminated by setWebhook" in str(e) or "Conflict" in str(e):
                    retry_count += 1
                    logger.warning(f"Webhook conflict detected (attempt {retry_count}/{max_retries}). Retrying...")
                    await asyncio.sleep(5)  # Wait before retry
                    
                    # Reset the handler state
                    TelegramHandler._started = False
                    handler = TelegramHandler()
                    handler = inject_fallback_services(handler)
                    if not hasattr(handler, 'watchlist_service'):
                        handler.watchlist_service = FallbackWatchlistService()
                    if not hasattr(handler, 'portfolio_service'):
                        handler.portfolio_service = FallbackPortfolioService()
                    if not hasattr(handler, 'trade_service'):
                        handler.trade_service = handler.portfolio_service
                    handler = patch_trading_commands(handler)
                    
                    if retry_count >= max_retries:
                        logger.error("Max retries reached. Unable to start bot due to webhook conflicts.")
                        raise
                else:
                    # Re-raise if it's not a webhook conflict
                    raise
            except KeyboardInterrupt:
                logger.info("Shutdown signal received")
                break
        
        # Cleanup
        logger.info("Shutting down bot...")
        monitor.stop()
        monitor_task.cancel()
        if hasattr(handler, 'stop'):
            await handler.stop()
        await runner.cleanup()
        logger.info("Bot shutdown complete")
    
    except ImportError as e:
        logger.error(f"Failed to import TelegramHandler: {e}")
        logger.error("Make sure all dependencies are installed")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Critical error: {e}")
        raise

if __name__ == "__main__":
    # Check for required environment variable
    if not os.getenv('TELEGRAM_API_TOKEN'):
        logger.error("TELEGRAM_API_TOKEN environment variable is required")
        sys.exit(1)
    
    # Run the bot
    asyncio.run(main())