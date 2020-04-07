from datetime import date, timedelta, datetime
import yfinance as yf
import pandas as pd
import numpy as np

from scraper import StockScraper
'''
Property of Andrew Sommer
March 24, 2020
Version 1.1

This version takes hardcoded inputs for certain stock tickers and writes the output of
their price and volume data for the past 5 trading days to an excel, with values for every 15 minute interval

v1.1 adds functionality to output whether or not the z-score is above the defined weighted moving average
'''

'''
'Packages needed:
'Pandas
'openpyxl
'yahoofinance
'''

# This function returns the last trading day for a specified number of days back


def get_trading_start_date(date, days_of_trading):
    first_trading_date = date - timedelta(days=days_of_trading)
    while first_trading_date.weekday() > 4: #Mon-Fri are 0-4
        first_trading_date -= timedelta(days=1)
    return first_trading_date

# begin program


# hardcoded for now, can add functionality for user input / to search a pre-set interest list
# allow for functionality to pull from robinhood?
tickers = "SPY aapl goog"


# f or now, it is 5 trading days prior, though this can be a user input as well
start_date = get_trading_start_date(date.today(), 5)

# for now it's 5 days, though this can be a user input as well
period = "5d"

# For now it's 15m, but that can be user input as well
interval = "15m"

data = yf.download("SPY", start_date=start_date, endDate=date.today(), group_by='ticker', period=period, interval=interval)
datas = yf.download(tickers, start_date=start_date, endDate=date.today(), group_by='ticker', period=period, interval=interval)



msft = yf.Ticker("MSFT")


if msft.financials.empty:
    scraper = StockScraper("MSFT")
    scraper.pull_all_data()
    financials = scraper.financials
else:
    financials = msft.financials


# Use pandas to write to excel
now = datetime.now().replace(tzinfo=None)
print(type("Stock pull at: " + now.strftime("%Y-%m-%d %H:%M:%S")))
#data.to_excel("Stock pull at: " + now.strftime("%Y-%m-%d %H:%M:%S")+".xlsx")


# pandas dataframe displayed as:
'''
Datetime      Open        High         Low       Close   Adj Close    Volume
'''


'''
#set up params for data
rows, cols = len(data.index), data.shape[1]

#This function returns the mean for the specified type, and number of days
#as of right now it's hardcoded with a weight that allows for 5 days, but the idea is to make it variable
def getMean(type, numDays):
    weights = {5/15,4/15,3/15,2/15,1/15}
    if (type is "simple weighted avg") :
        for x in range(len(weights)):
            #need to calculate an average for last 5 trading days close
            mean += weights[x]
    return mean

mean = getMean("simple weighted avg", int(period[0]))
#SD =
zScore = (data[rows-1][cols-1] - mean)/SD



#implement the Altman z-score as well?
'''
