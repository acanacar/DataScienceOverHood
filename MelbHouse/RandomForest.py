import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Path
file_path = '/home/cem/PycharmProjects/DataScienceOverHood/MelbHouse/train.csv'
# DF
house_data = pd.read_csv(file_path)
# y
y = house_data.SalePrice
# X
features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = house_data[features]
# Split
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

# Model
house_rforest_model = RandomForestRegressor(random_state=1)

# Fit
house_rforest_model.fit(train_X, train_y)

# MAE
val_predictions = house_rforest_model.predict(val_X)
val_mae = mean_absolute_error(val_y, val_predictions)
print('Validation MAE for Random Forest Model : {:,.0f}'.format(val_mae))
