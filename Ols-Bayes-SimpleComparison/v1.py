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


'''
# compare indexes
(data / data.ix[0] * 100).plot(figsize=(12,12))
plt.title("Standarized Indexes 1990-2016")
plt.show()
'''

# predict next year's price
stockA['Future'] = stockA['Open'].shift(-252)

# drop Nan
stockA = stockA.dropna()

train = stockA.loc[stockA.index < '12-31-2015']
test = stockA.loc[stockA.index > '12-31-2015']

# prep for data for classifiers
x = train['Open'].as_matrix()
y = train['Future'].as_matrix()

x_test = test['Open'].as_matrix()
y_test = test['Future'].as_matrix()

# reshape into (row, column for sklearn)
x = x.reshape((len(x), 1))
y = y.reshape((len(y), 1))

x_test = x_test.reshape(len(x_test), 1)
y_test = y_test.reshape(len(y_test), 1)

# fit classifiers
ols = LinearRegression()
ols = ols.fit(x, y)
predict_ols = ols.predict(x_test)
score_ols = ols.score(x_test, y_test)

clf = BayesianRidge(compute_score=True)
clf = clf.fit(x, y)
predict_b = clf.predict(x_test)
score_b = clf.score(x_test, y_test)

print("Accuracy: OLS %lf, Bayes %lf" % (score_ols, score_b))

# plot results
plt.plot(y_test, 'r+', label="actual")
plt.plot(predict_ols, 'bx', label="ols")
plt.plot(predict_b, 'g1', label="bayesian")
plt.legend()
plt.title("Predict stockA 1 year ahead ( 2016 )")
plt.savefig('./OLS_vs_BayesianRegression.png')
plt.show()
