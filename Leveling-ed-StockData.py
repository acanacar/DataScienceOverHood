#True

# Level data so series is stationary in time
# take log of data
# save it to use in deconstructing signal to find anomolies
# Using finance.yahoo.com Nasdaq, S&P, DJI 1985 - date (Nov 29 2017)
#

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# pandas display options
pd.options.display.max_rows = 10000
pd.options.display.max_columns = 25
pd.options.display.width = 1000



######################################################################
# plot dataframe
########################################################################
def plot_dataframe(d, t):


    plt.figure(figsize=(18,18))
    plt.plot(d['NASDAQ'], label='NASDAQ')
    plt.plot(d['S&P'], label='S&P')
    plt.plot(d['DJIA'], label='DJIA')
    plt.plot(d['BTC'], label='BTC')
    plt.plot(d['Russell'], label='Russell')
    plt.title(t)
    plt.legend(loc='best')
    plt.show()


######################################################################
# data
########################################################################
# read in datafile created in LoadAndMatchDates.py
data = pd.read_csv('../data/StockDataWithVolume.csv', index_col='Date', parse_dates=True)
features = ['DJIA', 'S&P', 'NASDAQ', 'Russell', 'BTC']

