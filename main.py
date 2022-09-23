# INF601 - Advanced Programing in Python
# Ryder Cook
# Mini Project 2

import os
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

fixed_df = pd.read_csv('data/coffee.csv', sep=';', parse_dates=['Date'], dayfirst=True, index_col='Date')
fixed_df['Close'].plot()
plt.show()


def closing_prices(symbol, period="1mo"):
    try:
        ticker = yf.Ticker(symbol)
        data = ticker.history(period)
        return data["Close"]
    except Exception as e:
        print("Failed to get required data.", e)


# Starbucks Stock Symbol
ticker = "SBUX"
# One month period
period = "2mo"
prices_data = closing_prices(ticker, period)
# Round the values
prices_list = [round(val, 2) for val in prices_data.tolist()]

sns.lineplot(data=prices_data)
sns.set_theme()
plt.xticks(rotation=30)
plt.title(f"Closing Prices for {ticker} and Coffee")
plt.show()
# Five stocks
#ticker_names = ["SBUX", "BROS"]
# Collect data from last 18 days
#data = yf.download(tickers=ticker_names, period="18d")


# Save plot as png in new folder
def new_direct(direct):
    # Only make folder if folder doesn't exists
    if not os.path.exists(direct):
        os.mkdir(direct)


# Get the closing prices from five stocks
#def closing_prices(ticker):
#    return [price for price in data['Adj Close'][ticker]]


# Draw the charts for five stocks and save to new folder
def draw_charts(tickers):
    chart_dir = "charts"
    new_direct(chart_dir)
    for ticker in tickers:
        sns.lineplot(data=prices_data)
        sns.set_theme()
        plt.xticks(rotation=30)
        plt.title(f"Closing Prices for {ticker} and Coffee")
        plt.show()
        # Save plot as png in new folder
        plt.savefig(os.path.join(chart_dir, f"{ticker}.png"))
        plt.close()


draw_charts(ticker)