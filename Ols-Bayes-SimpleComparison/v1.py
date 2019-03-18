import pandas as pd
import numpy as np
from scipy import stats
from sklearn.linear_model import BayesianRidge, LinearRegression
import matplotlib.pyplot as plt
import sys


# read in file
def read_data(file_name):
    stock = pd.read_csv(file_name, parse_dates=True, index_col=0)  # 31747 days of data
    # remove samples with NAN values
    stock = stock.dropna(axis=0)
    # from newest to oldest to oldest to newest
    stock = stock.iloc[::-1]
    stock = stock[['Open']]
    # trim dates
    stock = stock.loc[stock.index > '01-01-2000']

    return stock


#############################################################################################
# load and combine stock indexes

path = '/home/cem/PycharmProjects/DataScienceOverHood/Ols-Bayes-SimpleComparison'
stockA = read_data('{}/stockA.csv'.format(path))
print("Loaded stockA", len(stockA))
stockB = read_data('{}/stockB.csv'.format(path))
print("Loaded stockB", len(stockB))
stockC = read_data('{}/stockC.csv'.format(path))
print("Loaded stockC", len(stockC))

# combine stock indexes into one dataframe
data = pd.concat([stockA['Open'], stockB['Open'], stockC['Open']], axis=1,
                 keys=['stockA', 'stockB', 'stockC'])
