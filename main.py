# INF601 - Advanced Programing in Python
# Ryder Cook
# Mini Project 2

import os
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Starbucks stock symbol
ticker_names = "SBUX"
# Collect data from last 22 years
data = yf.download(tickers=ticker_names, period="22y")
# Data set from Kaggle - Coffee prices last 22 years
coffeePrice = pd.read_csv('data/coffee.csv', index_col='Date', parse_dates=True)


# Save plot as png in new folder
def new_direct(direct):
    # Only make folder if folder doesn't exists
    if not os.path.exists(direct):
        os.mkdir(direct)


# Get the closing prices from five stocks
def closing_prices():
    return [price for price in data['Adj Close']]


# Draw the charts for five stocks and save to new folder
def draw_charts(tickers):
    chart_dir = "charts"
    new_direct(chart_dir)
    for ticker in tickers:
        ticker_price = np.array(closing_prices())
        plt.plot(ticker_price, label='Starbucks', color='g')
        plt.plot(coffeePrice.Close, label='Coffee', color='y')
        # Fancy chart output
        plt.title(f"Coffee VS Starbucks Closing Prices")
        plt.xlabel("22 Years")
        plt.ylabel("Price (USD)")
        plt.legend()
        # Save plot as png in new folder
        plt.savefig(os.path.join(chart_dir, f"CoffeeComparison.png"))
        plt.close()


draw_charts(ticker_names)
