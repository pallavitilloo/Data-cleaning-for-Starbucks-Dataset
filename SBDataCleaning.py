import numpy as np
import pandas as pd

# Data Cleaning Operations for Starbucks dataset
# https://www.kaggle.com/starbucks/starbucks-menu

data = pd.read_csv('starbucks_drinkMenu_expanded_WIP.csv')

# Operation 1: Fill missing values of "Caffeine" with Mean value

data['Caffeine (mg)'] = data['Caffeine (mg)'].fillna('varies')
df = data[(data['Caffeine (mg)'] != 'varies') & (data['Caffeine (mg)'] != 'Varies')].dropna()
df = np.asarray(df['Caffeine (mg)'], dtype=np.float)
caffeine_mean = round(df.mean())
data['Caffeine (mg)'][(data['Caffeine (mg)'].isin(['', 'Nan', 'varies', 'Varies']))] = caffeine_mean

# Operation 2: Correct wrong value of 'Total Fat (g)'

fat_correction = 32
data[' Total Fat (g)'][data[' Total Fat (g)'] == '3 2'] = fat_correction

# Operation 3: Correct format of data for DV% columns - remove '%' from column values

data['Vitamin A (% DV) '] = data['Vitamin A (% DV) '].str.replace(r'%$', '')
data['Vitamin C (% DV)'] = data['Vitamin C (% DV)'].str.replace(r'%$', '')
data[' Calcium (% DV) '] = data[' Calcium (% DV) '].str.replace(r'%$', '')
data['Iron (% DV) '] = data['Iron (% DV) '].str.replace(r'%$', '')

# Operation 4: Resolve data inconsistency by filling in SIZE values for Beverage Prep column
# to make it uniquely identifiable

bev_init_size = ''

for index, row in data.iterrows():
    bev_prep = row['Beverage_prep']
    if bev_prep.startswith('Short'):
        bev_init_size = 'Short'
    elif bev_prep.startswith('Tall'):
        bev_init_size = 'Tall'
    elif bev_prep.startswith('Grande'):
        bev_init_size = 'Grande'
    elif bev_prep.startswith('Venti'):
        bev_init_size = 'Venti'
    elif bev_prep == 'Solo' or bev_prep == 'Doppio':
        continue
    else:
        data['Beverage_prep'][index] = bev_init_size + " " + bev_prep

# Update clean data back into CSV

data.to_csv('starbucks_drinkMenu_expanded_WIP.csv', index = False)


