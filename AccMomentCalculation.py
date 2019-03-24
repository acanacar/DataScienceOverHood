# Attempt to use velocity, acceleration, momentum
# to predict prices 1 week, month, quarter into the future
# test date is 1/9/2017 using data from 1 week, month and quarter ago
# score seems insanely too good to be true.


import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split, cross_val_predict
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Constants
##########################################################################################################

# pandas display options
pd.options.display.max_rows = 100
pd.options.display.max_columns = 25
pd.options.display.width = 1000

one_day = 1
one_week = 5
one_month = 21
one_quarter = 63

# data to use in training and predictions
features = ['Close', 'Volume', 'dx', 'd2x', 'momentum']  # today's close


# features = ['Volume', 'dx', 'd2x',  'momentum', 'dx_abs', 'd2x_abs'] # no base price

