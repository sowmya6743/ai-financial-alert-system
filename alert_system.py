"""
AI Financial Alert System
Session 3: Multiple Stocks & Alert Conditions
"""

import yfinance as yf
from datetime import datetime

# List of stocks to track (ticker symbol, company name, alert threshold)
# Think of this as your watchlist — stocks you care about
stocks = [
    {"ticker": "AAPL", "name": "Apple", "alert_price": 280.00},
    {"ticker": "GOOGL", "name": "Google", "alert_price": 170.00},
    {"ticker": "MSFT", "name": "Microsoft", "alert_price": 430.00},
    {"ticker": "AMZN", "name": "Amazon", "alert_price": 190.00},
]

# Get current timestamp
# Like signing and dating a letter — you know exactly when this data was pulled
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print("=" * 50)
print(f"🤖 AI FINANCIAL ALERT SYSTEM")
print(f"📅 Time: {current_time}")
print("=" * 50)
print()

# Loop through each stock (check them one by one)
for stock in stocks:
    ticker = stock["ticker"]
    name = stock["name"]
    alert_price = stock["alert_price"]
    
    try:
        # Fetch current price from Yahoo Finance
        yf_ticker = yf.Ticker(ticker)
        current_price = yf_ticker.info.get('regularMarketPrice', 'N/A')
        
        if current_price != 'N/A':
            print(f"📊 {name} ({ticker}): ${current_price:.2f}")
            
            # ALERT CONDITION: Check if price crossed the threshold
            if current_price > alert_price:
                print(f"   🚨 ALERT! {name} is above ${alert_price:.2f} (Current: ${current_price:.2f})")
            else:
                print(f"   ✅ No alert. Below ${alert_price:.2f}")
        else:
            print(f"⚠️ Could not fetch price for {name} ({ticker})")
            
    except Exception as e:
        print(f"❌ Error fetching {name} ({ticker}): {e}")
    
    print()  # Empty line between stocks

print("=" * 50)
print("✅ Scan complete!")
print("=" * 50)