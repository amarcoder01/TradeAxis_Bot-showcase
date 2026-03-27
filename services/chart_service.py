"""
Chart Service - Generate dynamic charts using Chart-IMG API exclusively
Provides professional visual analysis for trading decisions
"""
import os
import asyncio
import aiohttp
from logger import logger

# Simple dependency checking without complex manager
try:
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    MATPLOTLIB_AVAILABLE = True
    logger.info("Matplotlib available for local chart generation")
except ImportError:
    plt = None
    mdates = None
    MATPLOTLIB_AVAILABLE = False
    logger.info("Matplotlib not available - using Chart-img API exclusively")

try:
    import pandas as pd
    PANDAS_AVAILABLE = True
    logger.info("Pandas available for data processing")
except ImportError:
    pd = None
    PANDAS_AVAILABLE = False
    logger.info("Pandas not available - simplified data handling")

try:
    import numpy as np
    NUMPY_AVAILABLE = True
    logger.info("Numpy available for calculations")
except ImportError:
    np = None
    NUMPY_AVAILABLE = False
    logger.info("Numpy not available - basic calculations only")

try:
    import yfinance as yf
    YFINANCE_AVAILABLE = True
    logger.info("YFinance available for data fetching")
except ImportError:
    yf = None
    YFINANCE_AVAILABLE = False
    logger.info("YFinance not available - Chart-img API only")
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
from io import BytesIO
import base64
from config import Config

class ChartService:
    """Service for generating trading charts and visual analysis"""
    
    def __init__(self):
        """Initialize chart service"""
        config = Config()
        self.chart_api_key = config.CHART_IMG_API_KEY
        logger.info("Chart service initialized")
    
    async def generate_price_chart(self, symbol: str, period: str = '1mo', interval: str = '1d') -> Optional[str]:
        """
        Generate a modern TradingView-style price chart using Chart-IMG API only. No fallback.
        """
        try:
            symbol = symbol.upper().strip()
            if not self.chart_api_key:
                logger.error("Chart-IMG API key not available. Cannot generate chart.")
                return None
            try:
                import aiohttp
                logger.info(f"Generating chart for {symbol} via Chart-IMG API (forced) - Period: {period}")
                
                # Chart-img API requires two parameters:
                # 1. interval: candle/bar timeframe (5m, 1H, 1D, etc.)
                # 2. range: time window to display (1D, 1M, 6M, etc.)
                
                # Map period to appropriate candle interval for Chart-img API
                # Chart-img API supported intervals: 1m, 5m, 15m, 30m, 1h, 4h, 1d, 1w, 1M
                if period in ['1d', '5d']:
                    chart_interval = '5m'  # 5-minute candles for daily view
                elif period in ['1w', '1wk']:
                    chart_interval = '1h'  # 1-hour candles for weekly view
                elif period in ['1mo', '1M']:
                    chart_interval = '1h'   # 1-hour candles for monthly view
                elif period in ['3mo', '3M', '3m']:
                    chart_interval = '4h'   # 4-hour candles for 3-month view
                elif period in ['6mo', '6M', '6m']:
                    chart_interval = '1D'   # Daily candles for 6-month view
                elif period in ['1y', '1Y', '12m', '2y', '5y']:
                    chart_interval = '1W'   # Weekly candles for yearly view
                elif period in ['1h']:
                    chart_interval = '1h'   # Direct mapping for hour intervals
                elif period in ['1min', '5min', '15min', '30min', '1hr']:
                    chart_interval = period.replace('min', 'm').replace('hr', 'h')
                else:
                    chart_interval = '1D'   # Default to daily candles
                
                # Map period to Chart-img range format (time window)  
                # Actually supported ranges from API testing: 1D, 5D, 1M, 3M, 6M, 1Y
                range_map = {
                    '1d': '1D', '5d': '5D', '1w': '5D', '1wk': '5D',  # Use 5D for weekly
                    '1mo': '1M', '1M': '1M', '3mo': '3M', '3M': '3M', '3m': '3M',
                    '6mo': '6M', '6M': '6M', '6m': '6M',
                    '1y': '1Y', '1Y': '1Y', '12m': '1Y',
                    '2y': '1Y', '5y': '1Y', '1h': '1D',  # Use 1Y for multi-year views
                    '1min': '1D', '5min': '1D', '15min': '1D', '30min': '1D', '1hr': '1D'
                }
                
                chart_range = range_map.get(period, '6M')
                
                logger.info(f"Chart-img API parameters: interval={chart_interval}, range={chart_range}, period={period}")
                if ':' not in symbol:
                    chartimg_symbol = f'NASDAQ:{symbol}'
                else:
                    chartimg_symbol = symbol
                url = 'https://api.chart-img.com/v2/tradingview/advanced-chart'
                headers = {
                    'x-api-key': self.chart_api_key,
                    'content-type': 'application/json'
                }
                payload = {
                    'symbol': chartimg_symbol,
                    'interval': chart_interval,  # Candle timeframe
                    'range': chart_range,        # Time window to display
                    'theme': 'dark',
                    'style': 'candle',
                    'width': 800,
                    'height': 600,
                    'studies': [
                        {'name': 'Volume'},
                        {'name': 'Relative Strength Index'},
                        {'name': 'MACD'}
                    ],
                    'timezone': 'America/New_York',
                    'format': 'png'
                }
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, headers=headers, json=payload, timeout=15) as resp:
                        logger.info(f"Chart-IMG API response status: {resp.status}")
                        if resp.status == 200:
                            img_bytes = await resp.read()
                            import base64
                            chart_b64 = base64.b64encode(img_bytes).decode()
                            logger.info(f"Chart-IMG chart generated successfully for {symbol}")
                            return chart_b64
                        else:
                            error_text = await resp.text()
                            logger.error(f"Chart-IMG API failed for {symbol}: {resp.status} {error_text}")
                            return None
            except Exception as e:
                logger.error(f"Chart-IMG API error for {symbol}: {e}")
                return None
        except Exception as e:
            logger.error(f"Error in generate_price_chart for {symbol}: {e}")
            return None
    
    async def generate_comparison_chart(self, symbols: List[str], period: str = '1mo') -> Optional[str]:
        """
        Generate comparison chart for multiple stocks
        
        Args:
            symbols (List[str]): List of stock symbols
            period (str): Time period
            
        Returns:
            Base64 encoded comparison chart or None if error
        """
        try:
            symbols = [s.upper().strip() for s in symbols[:5]]  # Limit to 5 stocks
            logger.info(f"Generating comparison chart for {symbols}")
            
            plt.style.use('dark_background')
            fig, ax = plt.subplots(figsize=(12, 8))
            
            colors = ['#00ff88', '#ff6b6b', '#4ecdc4', '#ffd93d', '#ff8c69']
            
            for i, symbol in enumerate(symbols):
                try:
                    ticker = yf.Ticker(symbol)
                    hist = ticker.history(period=period)
                    
                    if not hist.empty:
                        # Normalize to percentage change
                        normalized = (hist['Close'] / hist['Close'].iloc[0] - 1) * 100
                        ax.plot(hist.index, normalized, color=colors[i % len(colors)], 
                               linewidth=2, label=symbol)
                except Exception as e:
                    logger.warning(f"Failed to fetch data for {symbol}: {e}")
            
            ax.set_title('Stock Performance Comparison', fontsize=16, color='white', pad=20)
            ax.set_ylabel('Change (%)', fontsize=12)
            ax.set_xlabel('Date', fontsize=12)
            ax.legend(loc='upper left')
            ax.grid(True, alpha=0.3)
            ax.axhline(y=0, color='white', linestyle='--', alpha=0.5)
            
            plt.xticks(rotation=45)
            plt.tight_layout()
            
            # Convert to base64
            buffer = BytesIO()
            plt.savefig(buffer, format='png', dpi=150, bbox_inches='tight',
                       facecolor='#1a1a1a', edgecolor='none')
            buffer.seek(0)
            
            chart_b64 = base64.b64encode(buffer.read()).decode()
            plt.close()
            
            logger.info("Comparison chart generated successfully")
            return chart_b64
            
        except Exception as e:
            logger.error(f"Error generating comparison chart: {e}")
            return None
    
    async def generate_sector_chart(self, sector_data: Dict) -> Optional[str]:
        """
        Generate sector performance chart
        
        Args:
            sector_data (Dict): Sector performance data
            
        Returns:
            Base64 encoded sector chart or None if error
        """
        try:
            if not sector_data.get('sectors'):
                return None
            
            logger.info("Generating sector performance chart")
            
            sectors = sector_data['sectors']
            names = [s['sector'] for s in sectors]
            changes = [s['change_percent'] for s in sectors]
            
            plt.style.use('dark_background')
            fig, ax = plt.subplots(figsize=(12, 8))
            
            # Color bars based on performance
            colors = ['#00ff88' if change >= 0 else '#ff6b6b' for change in changes]
            
            bars = ax.barh(names, changes, color=colors, alpha=0.8)
            
            # Add value labels on bars
            for i, (bar, change) in enumerate(zip(bars, changes)):
                ax.text(bar.get_width() + (0.1 if change >= 0 else -0.1), bar.get_y() + bar.get_height()/2,
                       f'{change:+.2f}%', ha='left' if change >= 0 else 'right', va='center',
                       fontweight='bold', color='white')
            
            ax.set_title('Sector Performance Today', fontsize=16, color='white', pad=20)
            ax.set_xlabel('Change (%)', fontsize=12)
            ax.grid(True, alpha=0.3, axis='x')
            ax.axvline(x=0, color='white', linestyle='-', alpha=0.5)
            
            plt.tight_layout()
            
            # Convert to base64
            buffer = BytesIO()
            plt.savefig(buffer, format='png', dpi=150, bbox_inches='tight',
                       facecolor='#1a1a1a', edgecolor='none')
            buffer.seek(0)
            
            chart_b64 = base64.b64encode(buffer.read()).decode()
            plt.close()
            
            logger.info("Sector chart generated successfully")
            return chart_b64
            
        except Exception as e:
            logger.error(f"Error generating sector chart: {e}")
            return None
    
    async def generate_portfolio_chart(self, portfolio_data: Dict) -> Optional[str]:
        """
        Generate portfolio allocation chart
        
        Args:
            portfolio_data (Dict): Portfolio data
            
        Returns:
            Base64 encoded portfolio chart or None if error
        """
        try:
            if not portfolio_data.get('positions'):
                return None
            
            logger.info("Generating portfolio allocation chart")
            
            positions = portfolio_data['positions']
            symbols = [p['symbol'] for p in positions]
            values = [p['market_value'] for p in positions]
            
            plt.style.use('dark_background')
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 8))
            
            # Pie chart
            colors = plt.cm.Set3(np.linspace(0, 1, len(symbols)))
            wedges, texts, autotexts = ax1.pie(values, labels=symbols, autopct='%1.1f%%',
                                              colors=colors, startangle=90)
            ax1.set_title('Portfolio Allocation', fontsize=14, color='white')
            
            # Bar chart with P&L
            pnl = [p['unrealized_pl'] for p in positions]
            bar_colors = ['#00ff88' if p >= 0 else '#ff6b6b' for p in pnl]
            
            bars = ax2.bar(symbols, pnl, color=bar_colors, alpha=0.8)
            ax2.set_title('Unrealized P&L by Position', fontsize=14, color='white')
            ax2.set_ylabel('P&L ($)', fontsize=12)
            ax2.grid(True, alpha=0.3, axis='y')
            ax2.axhline(y=0, color='white', linestyle='-', alpha=0.5)
            
            plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45)
            plt.tight_layout()
            
            # Convert to base64
            buffer = BytesIO()
            plt.savefig(buffer, format='png', dpi=150, bbox_inches='tight',
                       facecolor='#1a1a1a', edgecolor='none')
            buffer.seek(0)
            
            chart_b64 = base64.b64encode(buffer.read()).decode()
            plt.close()
            
            logger.info("Portfolio chart generated successfully")
            return chart_b64
            
        except Exception as e:
            logger.error(f"Error generating portfolio chart: {e}")
            return None
    
    async def generate_chart_via_api(self, chart_config: Dict) -> Optional[str]:
        """
        Generate chart using Chart-IMG API (if available)
        
        Args:
            chart_config (Dict): Chart configuration
            
        Returns:
            Chart URL or None if error
        """
        try:
            if not self.chart_api_key:
                logger.warning("Chart-IMG API key not available")
                return None
            
            logger.info("Generating chart via Chart-IMG API")
            
            # Chart-IMG API integration would go here
            # This is a placeholder for the actual API integration
            
            return None
            
        except Exception as e:
            logger.error(f"Error generating chart via API: {e}")
            return None