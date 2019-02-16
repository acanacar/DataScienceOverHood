import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

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
house_model = DecisionTreeRegressor(random_state=1)

# Fit
house_model.fit(train_X, train_y)

# MAE
val_predictions = house_model.predict(val_X)
val_mae = mean_absolute_error(val_y, val_predictions)
print('Validation MAE : {:,.0f}'.format(val_mae))


def get_mae(max_leaf_nodes, train_X, train_y, val_X, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return mae


candidate_max_leaf_nodes = [5, 25, 50, 100, 250, 500]
# Write loop to find the ideal tree size from candidate_max_leaf_nodes
Maes = {}
for node in candidate_max_leaf_nodes:
    mae = get_mae(max_leaf_nodes=node, train_X=train_X, val_X=val_X, train_y=train_y, val_y=val_y)
    Maes[node] = mae

# Store the best value of max_leaf_nodes (it will be either 5, 25, 50, 100, 250 or 500)
best_tree_size = min(Maes, key=Maes.get)
print('best_tree_size: ', best_tree_size)

final_model = DecisionTreeRegressor(max_leaf_nodes=best_tree_size, random_state=1)
final_model.fit(X, y)

