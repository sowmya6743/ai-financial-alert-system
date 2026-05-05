"""
AI Financial Alert System
Session 2: Fetching real stock prices from Yahoo Finance
"""

import yfinance as yf

# Define the stock ticker symbol
# AAPL = Apple Inc. (you can change this later)
ticker_symbol = "AAPL"

# Create a ticker object
# Think of this as "connecting" to Apple's page on Yahoo Finance
stock = yf.Ticker(ticker_symbol)

# Fetch today's data
# Get the current price (latest closing price)
current_price = stock.info.get('regularMarketPrice', 'Not available')

# Display the result
print(f"📈 {ticker_symbol} Stock Price: ${current_price}")
print("✅ Stock data fetched successfully!")
