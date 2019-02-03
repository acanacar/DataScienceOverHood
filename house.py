import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
import seaborn as sns
import statsmodels.api as sm

boston_data = load_boston()

df = pd.DataFrame(boston_data.data, columns=boston_data.feature_names)
X = df
y = boston_data.target

X_constant = sm.add_constant(X)

model = sm.OLS(y, X_constant)
lr = model.fit()
lr.summary()

import statsmodels.formula.api as smf

dir(smf)

form_lr = smf.ols(formula='y ~ CRIM + ZN + INDUS + CHAS + NOX + RM  + AGE + DIS + RAD + TAX + PTRATIO+ B +LSTAT',data=df)
mlr = form_lr.fit()

mlr.summary()


pd.options.display.float_format = '{:,.4f}'.format

corr_matrix = df.corr()
corr_matrix

corr_matrix[np.abs(corr_matrix)<0.6] = 0
corr_matrix

plt.figure(figsize=(16,10))

sns.set(style='white')

# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)
sns.heatmap(corr_matrix,
            annot=True,
            cmap=cmap,
            vmax=.3,
            center=0,
            linewidths=.5,
            cbar_kws={"shrink": .5},
            annot_kws={"size": 7})
plt.show()