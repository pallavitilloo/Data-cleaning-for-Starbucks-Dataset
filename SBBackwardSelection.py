import pandas as pd

# Dimensionality Reduction for Starbucks dataset
# https://www.kaggle.com/starbucks/starbucks-menu

data = pd.read_csv('starbucks_drinkMenu_expanded_Nutrition.csv')

numeric = data.select_dtypes(include=['float64', 'int64'])

# Use Variance values for backward selection

var = numeric.var()
numeric = numeric.columns
variable = []

for i in range(0, len(var)):
    if var[i] < 250:
        variable.append(numeric[i])

print(variable)
# data = data.drop(variable, axis=1)
# data = data.drop(['Unnamed: 0'], axis=1)
# data.to_csv('starbucks_drinkMenu_expanded_Nutrition_WIP.csv', index=False)
