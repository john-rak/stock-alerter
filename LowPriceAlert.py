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

from datetime import date, timedelta, datetime
import yfinance as yf

def get_Trading_StartDate(aDate, daysBack):
    aDate -= timedelta(days=daysBack)
    while aDate.weekday() >4: #Mon-Fri are 0-4
        aDate-= timedelta(days=1)
    return aDate

#begin program



#hardcoded for now, can add functionality for user input / to search a pre-set interest list
#allow for functionality to pull from robinhood?
tickers = "SPY"

#for now, it is 5 trading days prior, though this can be a user input as well
startDate = get_Trading_StartDate(date.today(), 5)

#for now it's 5 days, though this can be a user input as well
period = "5d"

#For now it's 15m, but that can be user input as well
interval = "15m"

data = yf.download(tickers,startDate,endDate=date.today(),period=period, interval=interval)
breakpoint()

#Use pandas to write to excel
now = datetime.now().replace(tzinfo=None)
print(type("Stock pull at: " + now.strftime("%Y-%m-%d %H:%M:%S")))
data.to_excel("Stock pull at: " + now.strftime("%Y-%m-%d %H:%M:%S")+".xlsx")


#pandas dataframe displayed as:
'''
Adj. Close      Close       High        Low     Open        Volume
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
