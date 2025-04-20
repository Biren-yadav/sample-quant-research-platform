# Quant Research Platform

A modular quantitative research platform for backtesting trading strategies with Python and Streamlit.

----Features----------

- Data Fetcher: Get OHLC data from Yahoo Finance
- Strategy Library: 
  - SMA Crossover (50/200)
  - [Your next strategy here]
- Backtesting Engine: 
  - Sharpe Ratio, Drawdown metrics
  - Interactive performance charts
- Risk Analysis: 
  - PyFolio tear sheets
  - Returns distributions
- Modern UI: 
  - Ticker selection
  - Date range controls
  - Real-time visualization

--------Project Structure---------
quant-research-platform/
├── frontend/ # Streamlit UI components
│ ├── app.py # Main dashboard
│ └── utils.py # UI helpers
├── backend/ # Quant logic
│ ├── data.py # Data fetching
│ ├── strategies.py # Trading strategies
│ ├── backtest.py # Backtesting core
│ └── analysis.py # Performance metrics
├── requirements.txt # Dependencies
└── README.md # You are here

##Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/quant-research-platform.git
   cd quant-research-platform

2. Create virtual environment:

python -m venv venv
source venv/bin/activate  # Linux/Mac

3. Install dependencies:

pip install -r requirements.txt

4. Usage

Run the Streamlit app:

streamlit run frontend/app.py

Then access:

http://localhost:8501 in your browser

