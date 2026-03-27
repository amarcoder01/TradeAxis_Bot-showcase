<div align="center">
  <h1>🤖 TradeAxis Bot</h1>
  <p><strong>The Ultimate Institutional-Grade Quantitative & AI Trading Companion for Telegram</strong></p>

  <p>
    <a href="https://python.org"><img src="https://img.shields.io/badge/Python-3.11+-blue.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python Version"></a>
    <a href="https://core.telegram.org/bots/api"><img src="https://img.shields.io/badge/Telegram-Bot_API-0088cc.svg?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram API"></a>
    <a href="https://openai.com/"><img src="https://img.shields.io/badge/AI-OpenAI_Powered-412991.svg?style=for-the-badge&logo=openai&logoColor=white" alt="OpenAI"></a>
    <a href="https://github.com/microsoft/qlib"><img src="https://img.shields.io/badge/Quant-Microsoft_Qlib-yellow.svg?style=for-the-badge" alt="Microsoft Qlib"></a>
    <a href="https://pytorch.org/"><img src="https://img.shields.io/badge/Deep_Learning-PyTorch-EE4C2C.svg?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch"></a>
    <a href="https://render.com/"><img src="https://img.shields.io/badge/Deploy-Render_Ready-success.svg?style=for-the-badge&logo=render&logoColor=white" alt="Render"></a>
  </p>
</div>

---

## 📑 Table of Contents
1. [Overview](#overview)
2. [Vision](#vision)
3. [Exhaustive Feature List](#exhaustive-feature-list)
4. [Tech Stack & Dependencies](#tech-stack--dependencies)
5. [System Architecture](#system-architecture)
   - [High-Level Topology](#high-level-topology)
   - [Database Schema](#database-schema)
6. [Core Logic & Data Flow](#core-logic--data-flow)
   - [Step-by-Step AI Analysis Execution](#step-by-step-ai-analysis-execution)
   - [Alert System Event Loop](#alert-system-event-loop)
7. [Complete Project Structure](#complete-project-structure)
8. [Comprehensive Setup Guide](#comprehensive-setup-guide)
9. [Detailed Usage Guide & Commands](#detailed-usage-guide--commands)
10. [API, Webhooks & Health Checks](#api-webhooks--health-checks)
11. [Troubleshooting & Debugging](#troubleshooting--debugging)
12. [Environment Variables Dictionary](#environment-variables-dictionary)
13. [Deployment Instructions](#deployment-instructions)
14. [Performance & Scalability](#performance--scalability)
15. [Roadmap](#roadmap)
16. [Author & License](#author--license)

---

## Overview

**TradeAxis Bot** is a monolithic, highly resilient, and extraordinarily advanced Telegram trading bot designed to bring Wall Street-level quantitative analysis and AI-driven market intelligence to retail traders. 

Unlike standard bots that simply fetch stock prices, TradeAxis Bot acts as an autonomous financial analyst. It ingests real-time market data, calculates advanced technical indicators, runs Microsoft Qlib quantitative machine learning models, dynamically retrains itself, and synthesizes the output into human-readable insights using OpenAI's Large Language Models (LLMs). It features a state-of-the-art vectorized memory system that learns from user interactions, ensuring hyper-personalized financial guidance.

Built on an asynchronous, event-driven architecture using `python-telegram-bot` and `aiohttp`, the bot guarantees lightning-fast execution, robust webhook conflict resolution, and fault-tolerant background processing.

---

## Vision

### Short-Term Vision
To completely eliminate the friction between retail investors and complex financial data. By providing an accessible, conversational interface within Telegram, users can instantly receive deep fundamental analysis, technical charting, and real-time alerts without needing to navigate clunky broker interfaces or pay for expensive Bloomberg terminals.

### Long-Term Vision
To evolve TradeAxis Bot into a fully autonomous, hyper-personalized AI hedge fund manager. Future iterations will automatically execute paper trades to backtest strategies, utilize multi-exchange API integrations for live execution, optimize portfolio allocations dynamically based on deep learning predictions, and democratize elite quantitative finance strategies for everyone globally.

---

## ✨ Exhaustive Feature List

### 🧠 Intelligent Memory System (ChatGPT-like Context)
*   **Semantic Memory Storage**: Utilizes NLP embeddings to remember user risk tolerance, favorite tickers, past queries, and conversational context.
*   **Memory Consolidation**: Automatically merges and updates related memories to maintain an accurate profile of the trader.
*   **Cross-Session Persistence**: Retains context across bot restarts, allowing for seamless continuation of complex financial discussions.

### Institutional Quantitative Analysis (Microsoft Qlib)
*   **Predictive AI Models**: Integrates Microsoft Qlib to run machine learning algorithms on historical OHLCV data.
*   **`/smart_signal` Engine**: Generates actionable buy/sell/hold signals based on advanced alpha factors.
*   **Auto-Trainer Daemon**: A background service (`auto_trainer.py`) that schedules daily (6 AM) and weekly model retraining to adapt to shifting market regimes.

### 🤖 AI-Powered Market Insights
*   **Fundamental Synthesis**: Ingests P/E ratios, market caps, 52-week highs/lows, and sends them to OpenAI to generate human-readable narratives.
*   **Sentiment Analysis**: Evaluates recent market trends and news momentum to gauge bullish or bearish sentiment.

### Fault-Tolerant Real-Time Alert Engine
*   **Background Polling**: A dedicated `AlertService` thread checks market conditions every 60 seconds.
*   **Multi-Condition Alerts**: Supports price threshold crosses (e.g., `AAPL above 150`) and technical crossovers.
*   **Guaranteed Delivery**: Queues Telegram notifications to ensure alerts are delivered even during high network latency.

### 📊 Advanced Technicals & Dynamic Charting
*   **Indicators Engine**: Calculates RSI, MACD, Bollinger Bands, EMA, SMA, and Stochastic Oscillators dynamically via `enhanced_technical_indicators.py`.
*   **Visual Charting**: Uses `matplotlib` to generate and send custom, headless-rendered price charts directly in the chat.

### Intelligent Portfolio Optimizer
*   **Asset Allocation**: Tracks user investments and simulates performance attribution.
*   **Risk Management**: Analyzes portfolio variance and suggests rebalancing strategies based on modern portfolio theory.

### Document Intelligence (OCR & PDF)
*   **Financial Report Parsing**: Upload PDF earnings reports or screenshot images. The bot utilizes `PyPDF2` and `pytesseract` to extract text, passing it to the AI for immediate summary and impact analysis.

### Resilient Infrastructure
*   **Webhook Monitor**: Actively resolves Telegram API `Conflict: terminated by other getUpdates request` errors by falling back to long-polling automatically.
*   **Rate Limiting & Caching**: Uses `cachetools` to aggressively cache `yfinance` API calls, preventing IP bans and ensuring sub-second response times.

---

## Tech Stack & Dependencies

The project relies on a robust stack tailored for heavy data processing and async network I/O.

### Core Frameworks & Web
*   **Python 3.11+**: The core language utilizing structural pattern matching and advanced async features.
*   **`python-telegram-bot` (v20.8+)**: Handles the complete Telegram Bot API, including inline keyboards, callbacks, and conversational handlers.
*   **`aiohttp` & `Gunicorn`**: Powers the non-blocking architecture, webhook endpoints, and the health check web server.
*   **`asyncio`**: Standard library for concurrent I/O operations.

### AI, Machine Learning & Quant
*   **`openai`**: Official client for GPT-4/GPT-3.5-turbo API interactions.
*   **`qlib`**: Microsoft's AI-oriented quantitative investment platform.
*   **`scikit-learn`, `numpy`, `pandas`**: Core data science stack for technical indicator computation and data normalization.
*   **`torch` (PyTorch)**: Underpins the deep learning models within the advanced quant strategies.
*   **`pytesseract`, `PyPDF2`, `pdf2image`**: Document parsing and OCR.

### Data, State & Infrastructure
*   **`yfinance`**: Real-time and historical market data acquisition.
*   **`asyncpg`, `sqlalchemy`**: Database ORM and async PostgreSQL driver.
*   **`cachetools`**: In-memory caching for API optimization.
*   **`prometheus-client`**: Exposes metrics for Grafana/Prometheus scraping.
*   **`schedule`, `apscheduler`**: Cron-like job scheduling for auto-training and alerts.

---

## System Architecture

TradeAxis Bot utilizes a modular, microservice-inspired monolithic architecture. Separation of concerns is strictly enforced between the presentation layer (Telegram UI), the business logic layer (Trading Intelligence, Quant Models), and the data access layer.

### High-Level Topology

```mermaid
graph TB
    subgraph Client
        User[Telegram Client]
    end

    subgraph Presentation Layer
        TG_Handler[telegram_handler.py\nCommand & Callback Router]
        UI_Builder[ui_components.py\nInline Keyboards & Formatting]
    end

    subgraph Business Logic / Core Services
        Router[Command Dispatcher]
        Intel[trading_intelligence.py\nAI Synthesis]
        Quant[qlib_service.py\nML Signal Engine]
        Mem[intelligent_memory_system.py\nVector Context]
        Port[portfolio_optimizer.py\nRisk Management]
        Chart[chart_service.py\nVisual Generation]
    end

    subgraph Background Daemons
        AlertMonitor[alert_service.py\n60s Poller Thread]
        Trainer[auto_trainer.py\nScheduled ML Retraining]
        WebHook[webhook_monitor.py\nConflict Resolution]
    end

    subgraph External APIs & Integrations
        OAI[OpenAI GPT-4]
        YF[Yahoo Finance API]
        Postgres[(PostgreSQL / SQLite)]
    end

    User <-->|Webhooks / Polling| TG_Handler
    TG_Handler <--> UI_Builder
    TG_Handler --> Router
    
    Router --> Intel
    Router --> Quant
    Router --> Mem
    Router --> Port
    Router --> Chart

    Intel --> OAI
    Intel --> YF
    Quant --> YF
    Chart --> YF

    AlertMonitor --> YF
    AlertMonitor -->|Push Notification| TG_Handler
    
    Trainer --> Quant

    Mem <--> Postgres
    AlertMonitor <--> Postgres
    Port <--> Postgres
```

### Database Schema
The system maintains user state, alerts, and vectorized memories.

```mermaid
erDiagram
    USERS {
        int id PK
        string telegram_id
        string username
        timestamp created_at
    }
    ALERTS {
        int id PK
        int user_id FK
        string symbol
        float target_price
        string condition "above/below"
        boolean is_active
    }
    MEMORIES {
        int id PK
        int user_id FK
        string memory_type "PREFERENCE/TRADING"
        text content
        blob embedding "Vector representation"
        float relevance_score
    }
    PORTFOLIO {
        int id PK
        int user_id FK
        string symbol
        float quantity
        float average_buy_price
    }
    
    USERS ||--o{ ALERTS : has
    USERS ||--o{ MEMORIES : generates
    USERS ||--o{ PORTFOLIO : owns
```

---

## Core Logic & Data Flow

### Step-by-Step AI Analysis Execution
When a user requests a deep analysis (`/analyze AAPL`), the system executes a complex orchestration pipeline:

1. **Input Validation & Normalization**: The `telegram_handler.py` catches the command, extracts the ticker "AAPL", and strips special characters.
2. **Context Retrieval (RAG)**: The `IntelligentMemorySystem` searches the `user_memories` table for the user's risk profile (e.g., "User prefers conservative dividend stocks").
3. **Async Data Fetching**: `MarketDataService` queries `yfinance` for live price, 52-week data, volume, and trailing 30-day OHLCV data. The result is cached via `cachetools` for 5 minutes.
4. **Technical Indicator Calculation**: The OHLCV array is passed to `enhanced_technical_indicators.py` to calculate RSI, MACD, and Support/Resistance levels natively via `numpy`/`pandas`.
5. **Prompt Engineering**: `trading_intelligence.py` constructs a massive context window combining:
   - Live Market Data
   - Technical Indicators
   - User Memory Context
   - System Prompt constraints (ensuring financial disclaimers are present).
6. **LLM Inference**: The prompt is dispatched asynchronously to the OpenAI API.
7. **UI Assembly**: The response is caught, injected with corresponding emojis and markdown formatting via `ui_components.py`, and attached to an Inline Keyboard (e.g., "📈 View Chart", "🔔 Set Alert").
8. **Delivery**: The final payload is transmitted back to the Telegram User.

### Alert System Event Loop

```mermaid
sequenceDiagram
    participant D as Daemon (alert_service.py)
    participant DB as Database
    participant MD as MarketDataService
    participant TG as Telegram API
    participant U as User

    loop Every 60 Seconds
        D->>DB: Fetch all active alerts
        activate DB
        DB-->>D: List of Alert Objects
        deactivate DB
        
        Note over D,MD: Group by Symbol to minimize API calls
        D->>MD: Batch fetch current prices
        activate MD
        MD-->>D: Dict of {Symbol: CurrentPrice}
        deactivate MD
        
        loop For each Alert
            alt Price Condition Met (e.g. Current > Target)
                D->>TG: send_message(User.ID, "🚨 ALERT TRIGGERED!")
                D->>DB: Mark Alert as Inactive/Triggered
            end
        end
    end
```

---

## Complete Project Structure

Below is the exhaustive, un-truncated file tree of the TradeAxis Bot repository, detailing every component that powers the application.

```text
TradeAxis_Bot/
├── attached_assets/                        # Directory for debug logs, error traces, and UI screenshots
│   ├── Pasted--...telegram-ext-Updater-ERROR...txt # Captured webhook conflict logs
│   ├── Screenshot...png                    # UI design references
│   └── menu issue...jpg                    # Documented UI bugs for tracking
├── deploy/                                 # 🚀 CORE PRODUCTION SOURCE CODE
│   ├── .github/
│   │   └── workflows/
│   │       └── main_tradeaxisbot.yml        # GitHub Actions CI/CD pipeline definition
│   ├── .gitignore                          # Deploy-specific git exclusions
│   ├── .render-buildpacks.rc               # Custom Render environment configuration
│   ├── .security_keys                      # Local keystore (git-ignored in prod)
│   ├── ADVANCED_FEATURES_SUMMARY.md        # Documentation on Qlib and ML implementations
│   ├── ALERT_SYSTEM_OPTIMIZATION_SUMMARY.md# Docs on the 60s background poller efficiency
│   ├── DEPLOYMENT.md                       # Comprehensive deployment instructions
│   ├── DEPLOYMENT_CHECKLIST.md             # Pre-flight checklist for production pushes
│   ├── DEPLOYMENT_READY_SUMMARY.md         # Status report on Render compatibility
│   ├── MEMORY_SYSTEM_README.md             # Deep dive into the vectorized memory RAG system
│   ├── PHASE3_COMPLETE_SUMMARY.md          # Roadmap tracking documentation
│   ├── Privacy_Policy.md                   # User privacy and data retention policy
│   ├── Procfile                            # Gunicorn process definition for Render/Heroku
│   ├── README (2).md                       # Legacy documentation
│   ├── RENDER_DEPLOYMENT.md                # Specific step-by-step for Render
│   ├── RENDER_DEPLOYMENT_FIXES.md          # Post-mortem on resolving Render build issues
│   ├── RENDER_SETUP_INSTRUCTIONS.md        # Quick-start Render docs
│   ├── SECURITY_IMPLEMENTATION_GUIDE.md    # API key and database security standards
│   ├── TYPING_INDICATOR_ENHANCEMENT.md     # UX improvements for async waiting states
│   ├── UI_MODERNIZATION_PLAN.md            # Strategy for inline keyboards and emojis
│   ├── USER_GUIDE_ADVANCED.md              # End-user manual for complex features
│   ├── advanced_bot.py                     # Wrapper for highly experimental bot features
│   ├── advanced_qlib_strategies.py         # Microsoft Qlib model definitions (Alpha158, etc.)
│   ├── alembic.ini                         # Database migration configuration
│   ├── alert_monitor.py                    # Standalone script for running alerts
│   ├── alert_performance_report.txt        # Benchmarks for alert execution times
│   ├── alert_service.py                    # CORE: The 60s polling engine and alert logic
│   ├── auto_trainer.py                     # CORE: Scheduled cron jobs for ML retraining
│   ├── backtesting_framework.py            # Engine to test strategies against historical data
│   ├── build.sh                            # CORE: Production build script (installs C++ deps)
│   ├── callback_handler.py                 # CORE: Routes inline keyboard button clicks
│   ├── chart_service.py                    # CORE: Matplotlib dynamic chart generator
│   ├── check_sys_path.py                   # Debug script for Python import paths
│   ├── code_quality_enhancements.py        # Linting and formatting standardizer
│   ├── command_patches.py                  # Hotfixes for legacy Telegram commands
│   ├── commands.py                         # Dictionary mapping of all bot commands
│   ├── config.py                           # CORE: Global configuration and environment loader
│   ├── conversation_memory.py              # Short-term chat history for contextual replies
│   ├── create_alert_table.py               # DB Schema initialization script
│   ├── create_tables.py                    # Full DB Schema initialization script
│   ├── current_packages.txt                # Dependency lock snapshot
│   ├── db.py                               # Async PostgreSQL connection manager
│   ├── db_cleanup.py                       # Maintenance script for orphaned database records
│   ├── db_simple.py                        # Fallback SQLite connection manager
│   ├── debug_*.py                          # Various specialized debugging scripts (alerts, callbacks)
│   ├── deep_learning_models.py             # PyTorch neural network definitions for price prediction
│   ├── dependency_wrapper.py               # Safe-import wrapper for optional heavy libraries
│   ├── deploy-render.ps1 / .sh             # CLI automation scripts for deployment
│   ├── deploy_bot.py                       # Alternative entry point for restricted environments
│   ├── deployment_status.md                # Live tracking of deployment health
│   ├── download_qlib_us_data.py            # Script to bootstrap historical Qlib data
│   ├── enhanced_*.py                       # V2 iterations of config, memory, monitoring, services
│   ├── final_main.py                       # Entry point variant
│   ├── fix_*.py                            # One-off migration scripts (encoding, BigInt migrations)
│   ├── gunicorn_config.py                  # Production WSGI/ASGI web server tuning
│   ├── health_check.py                     # Ping endpoint logic for Render load balancers
│   ├── input_validator.py                  # Sanitization for user inputs (preventing injection)
│   ├── intelligent_memory_system.py        # CORE: Vectorized semantic memory storage
│   ├── logger.py                           # CORE: Structured, colorized logging formatter
│   ├── main.py                             # CORE: Production Application Entry Point
│   ├── market_data_service.py              # CORE: yfinance wrapper, cache, and normalization
│   ├── memory_*.py                         # Utilities for memory integration and optimization
│   ├── minimal_main.py / minimal_start.py  # Stripped-down entry points for debugging
│   ├── models.py                           # SQLAlchemy ORM class definitions
│   ├── monitor_deployment.ps1              # Local powershell monitor for deployment
│   ├── monitoring.py                       # Prometheus metrics exporter
│   ├── openai_service.py                   # CORE: Wrapper for OpenAI API interactions
│   ├── performance_*.py                    # Caching logic and performance attribution
│   ├── portfolio_*.py                      # Logic for tracking user holdings and risk
│   ├── qlib_ai_portfolio_pipeline.py       # Integration between Qlib signals and user portfolios
│   ├── qlib_service.py                     # CORE: Microsoft Qlib initialization and inference
│   ├── rate_limiter.py                     # Protection against API abuse and spam
│   ├── real_market_data.py                 # Live websocket streamer (where supported)
│   ├── render.yaml                         # CORE: Infrastructure-as-Code for Render.com
│   ├── requirements.txt                    # CORE: Production Python dependencies
│   ├── run_*.py / start_*.py / start.sh    # Various shell and python startup permutations
│   ├── secure_logger.py / security_*.py    # Middleware for sanitizing logs and request validation
│   ├── telegram_handler.py                 # CORE: The primary python-telegram-bot Application
│   ├── timezone_utils.py                   # Normalizes UTC/IST to prevent APScheduler crashes
│   ├── trade_service.py                    # Executes simulated paper trades
│   ├── trading_intelligence.py             # CORE: Orchestrates Data + Technicals + OpenAI
│   ├── ui_components.py                    # CORE: Standardized UI generation (keyboards, messages)
│   └── webhook_monitor.py                  # CORE: Daemon that resolves Telegram Webhook Conflicts
├── .dockerignore                           # Excludes local files from Docker builds
├── .env.example                            # Template for environment variables
├── .gitignore                              # Standard git exclusions
├── .replit                                 # Configuration for Replit IDE
├── DEPLOYMENT.md                           # Root-level deployment guide
├── Procfile                                # Root-level Gunicorn process definition
├── README.md                               # THIS FILE
├── deploy.json                             # Deployment metadata
├── deploy_cleanup.sh                       # Script to prune root directory before pushing
├── main.py                                 # Root local development entry point
├── pyproject.toml                          # PEP 621 Python project metadata
├── runtime.txt                             # Specifies `python-3.11.x` for PaaS providers
├── uv.lock                                 # UV extremely fast python package manager lockfile
└── test_*.py / demo_*.py / resilient_*.py  # Root level test suites and isolated run environments
```

---

## Comprehensive Setup Guide

### 1. Prerequisites
Ensure you have the following installed on your local machine:
*   **Python 3.11** or higher.
*   **Git** for version control.
*   *(Optional but Recommended)* **C++ Build Tools**: Required on Windows if you intend to run Microsoft Qlib locally.
*   **Telegram Account**: To interact with BotFather.
*   **OpenAI Account**: To generate an API Key.

### 2. Procure API Keys
1.  **Telegram Token**: Message [@BotFather](https://t.me/botfather) on Telegram, send `/newbot`, follow the prompts, and copy the `HTTP API Token`.
2.  **OpenAI Key**: Visit the [OpenAI API Dashboard](https://platform.openai.com/api-keys) and generate a new secret key.

### 3. Clone and Environment Setup

```bash
# Clone the massive repository
git clone https://github.com/your-username/TradeAxis_Bot.git
cd TradeAxis_Bot

# Initialize a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install the heavy production dependencies
# (This may take several minutes due to torch, pandas, and qlib)
pip install -r deploy/requirements.txt
```

### 4. Configuration
Duplicate the environment template:
```bash
cp deploy/.env.example .env
```
Open `.env` in your text editor and populate the critical variables:
```env
TELEGRAM_API_TOKEN=your_bot_token_here
OPENAI_API_KEY=sk-your_openai_api_key_here
TELEGRAM_POLLING_MODE=true  # Crucial for local testing to avoid webhook requirements
```

### 5. Launching the Bot
Because the project is architected for production, the safest way to run it locally is using the `deploy` module's entry point:

```bash
# Run the main entry point
python main.py
```
*You should see output indicating the `TradeMaster AI Bot` has started, the webhook monitor is active, and the health server is listening on port 5000.*

---

## Detailed Usage Guide & Commands

Interact with TradeAxis Bot by sending commands directly in your Telegram chat. The bot features an intuitive UI using Inline Keyboards, so you rarely have to type commands manually after `/start`.

### Core Commands

| Command | Syntax Example | Deep Description |
| :--- | :--- | :--- |
| **`/start`** | `/start` | Registers your Telegram ID in the database, establishes your default vectorized memory profile, and renders the rich Main Menu UI with interactive buttons. |
| **`/help`** | `/help` | Displays a formatted, contextual list of all available commands and their arguments. |
| **`/price`** | `/price TSLA` | Bypasses AI generation for raw speed. Instantly returns current price, daily absolute change, percentage change, and daily volume using `yfinance`. |
| **`/analyze`** | `/analyze NVDA` | **The flagship feature.** Calculates RSI, MACD, Support/Resistance, fetches 52w highs/lows, and sends the payload to OpenAI. Returns a comprehensive, multi-paragraph markdown report detailing fundamental and technical health. |
| **`/smart_signal`** | `/smart_signal MSFT`| Invokes the `QlibService`. Evaluates the ticker against pre-trained ML models (like Alpha158) to output a quantitative probability score and a definitive `BUY`, `SELL`, or `HOLD` signal. |

### Alert & Portfolio Management

| Command | Syntax Example | Deep Description |
| :--- | :--- | :--- |
| **`/alert`** | `/alert BTC above 90000` | Registers a trigger in the database. The `alert_service.py` daemon will poll this every 60 seconds. When BTC crosses 90k, you receive an immediate push notification. |
| **`/alerts`** | `/alerts` | Retrieves all active alerts from the database and renders them with inline `[Delete]` callback buttons for easy management. |
| **`/portfolio`** | `/portfolio` | Displays your current tracked holdings, calculating real-time PnL (Profit and Loss), total equity, and risk distribution. |

### Document Parsing
*   **File Uploads**: Simply drag and drop a PDF (e.g., a 10-K Earnings Report) or an image into the chat. The bot automatically intercepts the file, runs OCR/Parsing, and feeds the text to OpenAI for an instant summary.

---

## API, Webhooks & Health Checks

For PaaS environments (Render, Heroku), applications must bind to a `$PORT` and respond to HTTP requests, otherwise the platform will kill the process.

TradeAxis Bot solves this by running an `aiohttp` web server concurrently with the Telegram bot loop.

*   **`GET /`**: Returns basic JSON metadata `{ "status": "healthy", "bot": "TradeMaster AI", "version": "2.0" }`.
*   **`GET /health`**: Used specifically by Render's load balancer to verify the container is alive.
*   **`GET /metrics`**: Exposes Prometheus-compatible text metrics. Tracks `api_requests_total`, `cache_hits`, `active_users`, and `alert_processing_time_ms`.

---

## Troubleshooting & Debugging

Given the complexity of the architecture, here are the most common pitfalls and their exact solutions.

### 1. Webhook Conflict (`Conflict: terminated by other getUpdates request`)
**Cause**: You have the bot running locally via long-polling, while a cloud server (or a stuck background process) is also trying to consume the webhook/polling stream. Telegram strictly enforces one listener per token.
**Solution**:
The bot includes `webhook_monitor.py` to handle this gracefully, but if it loops:
1. Revoke your token via BotFather and update your `.env`.
2. Or, run a script to manually delete the webhook: `https://api.telegram.org/bot<YOUR_TOKEN>/deleteWebhook?drop_pending_updates=true`.

### 2. Timezone/APScheduler Crashes (`ValueError: offset-naive datetime`)
**Cause**: `python-telegram-bot`'s `JobQueue` uses `APScheduler`, which strictly requires timezone-aware datetimes, but server environments often default to naive UTC.
**Solution**: This is patched in `telegram_handler.py` using `os.environ['TZ'] = 'UTC'` and monkey-patching `apscheduler.util.astimezone`. Ensure your system allows environment variable overrides.

### 3. Microsoft Qlib Installation Failures (Windows)
**Cause**: Qlib requires compiling C++ extensions (`Cython`, `numpy`).
**Solution**: 
1. Install [Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) and select the "Desktop development with C++" workload.
2. Alternatively, use WSL2 (Windows Subsystem for Linux) or run the project via Docker.

### 4. High Memory Usage / Render OOM Kills
**Cause**: Loading PyTorch, Qlib models, and `yfinance` pandas dataframes simultaneously can exceed the 512MB RAM limit on free PaaS tiers.
**Solution**: In `deploy/requirements.txt`, ensure you are using CPU-only versions of PyTorch (`--extra-index-url https://download.pytorch.org/whl/cpu`).

---

## 🔐 Environment Variables Dictionary

An exhaustive list of configurations supported by `config.py`:

| Variable | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| `TELEGRAM_API_TOKEN` | String | ✅ | Your bot's unique authentication token. |
| `OPENAI_API_KEY` | String | ✅ | Authentication for LLM inference. |
| `DATABASE_URL` | String | ❌ | Connection string (e.g., `postgresql+asyncpg://user:pass@host/db`). Falls back to `sqlite:///bot_database.db`. |
| `PORT` | Integer | ❌ | HTTP port for the health server. Defaults to `5000` or `8080`. |
| `TELEGRAM_POLLING_MODE`| Boolean | ❌ | If `true`, forces `getUpdates` instead of webhooks. Mandatory for local dev. |
| `REDIS_URL` | String | ❌ | Optional Redis connection for distributed caching across multiple bot workers. |
| `LOG_LEVEL` | String | ❌ | `DEBUG`, `INFO`, `WARNING`, `ERROR`. Defaults to `INFO`. |
| `MAX_ALERTS_PER_USER` | Integer | ❌ | Caps the database to prevent abuse. Defaults to `10`. |

---

## Deployment Instructions

TradeAxis Bot is heavily optimized for continuous deployment.

### Option A: Render.com (Recommended)
The repository includes a `render.yaml` Infrastructure-as-Code blueprint.
1. Fork the repository to your GitHub account.
2. Log in to [Render](https://render.com) and click **New -> Blueprint**.
3. Select your repository. Render will read `render.yaml` and automatically configure the Web Service, Build Command (`./deploy/build.sh`), and Start Command (`gunicorn deploy.main:app --worker-class aiohttp.GunicornWebWorker --bind 0.0.0.0:$PORT`).
4. Enter your Environment Variables in the Render dashboard.
5. Deploy.

### Option B: Docker Deployment
For VPS (DigitalOcean, AWS, Linode) or self-hosting:
1. Create a `Dockerfile`:
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY deploy/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```
2. Build and Run:
```bash
docker build -t tradeaxis-bot .
docker run -d --env-file .env -p 5000:5000 tradeaxis-bot
```

---

## ⚡ Performance & Scalability

TradeAxis Bot is engineered to handle massive scale without blocking the main event loop.

1. **Fully Asynchronous Architecture**: By utilizing `asyncio` and `aiohttp`, a single Python process can handle thousands of concurrent Telegram connections. Network calls to OpenAI and Yahoo Finance use `await`, freeing the CPU to process other users' commands.
2. **Aggressive In-Memory Caching**: `cachetools.TTLCache` is implemented around the `yfinance` fetchers. If 100 users request `/price AAPL` within 60 seconds, only *one* network call is made to Yahoo Finance; the other 99 are served instantly from RAM (0.01ms response time).
3. **Optimized Polling**: The `AlertService` does not fetch data per user. It groups all active alerts by symbol (e.g., pulling the price of `BTC` once, then evaluating 50 different users' alerts against that single price variable), massively reducing rate-limit risks.

---

## Roadmap

TradeAxis Bot is in active, aggressive development.

- [x] **Phase 1: Foundation** - Async architecture, core commands, yfinance integration, UI/UX modern inline keyboards.
- [x] **Phase 2: Intelligence** - OpenAI fundamental analysis, dynamic matplotlib charting, OCR document parsing.
- [x] **Phase 3: Quantitative Edge** - Microsoft Qlib integration, background alert poller, vectorized semantic memory engine.
- [ ] **Phase 4: Personalization (Q3 2025)** - Custom web-dashboards linked via Telegram WebApps, granular favorite stock watchlists, customized risk-tolerance sliders.
- [ ] **Phase 5: Multi-Exchange Crypto Support (Q4 2025)** - Integration with Binance, Bybit, and Coinbase APIs via CCXT for live crypto tape reading.
- [ ] **Phase 6: Autonomous Execution (Q1 2026)** - Automated paper trading, backtesting framework UI integration, and eventually live API execution based on Qlib signals.

---

## Author & License

Built with extreme dedication and ❤️ by **TradeAxis** and Open Source Contributors.

This project is licensed under the **MIT License**. You are free to use, modify, and distribute this software, provided that the original copyright notice and permission notice are included in all copies or substantial portions of the software.
