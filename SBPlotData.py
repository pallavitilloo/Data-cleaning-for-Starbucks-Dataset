import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


def get_outliers(a):
    q1 = np.percentile(a, 25)
    q3 = np.percentile(a, 75)
    iqr = q3 - q1
    outlier = 1.5 * iqr
    return outlier


plt.style.use('seaborn')

data = pd.read_csv('starbucks_drinkMenu_expanded_WIP.csv', encoding='UTF-16', sep=',', skipinitialspace=True)

food = data['Item']
cal = data['Calories']
fat = data['Fat (g)']
carb = data['Carb. (g)']
fibre = data['Fiber (g)']
protein = data['Protein (g)']

dv_fat = round(100.0 * fat / rdv_Fat)
dv_carb = round(100.0 * carb / rdv_Carb)
dv_fibre = round(100.0 * fibre / rdv_Fiber)
dv_protein = round(100.0 * protein / rdv_Protein)

data['Fat (%DV)'] = dv_fat
data['Carb. (%DV)'] = dv_carb
data['Fiber (%DV)'] = dv_fibre
data['Protein (%DV)'] = dv_protein

data.to_csv('starbucks-menu-nutrition-food-new.csv', index=False)

# Get outlier value
arr_fat = np.asarray(fat)
out_fat = get_outliers(arr_fat)

arr_carb = np.asarray(carb)
out_carb = get_outliers(arr_carb)

arr_fibre = np.asarray(fibre)
out_fibre = get_outliers(arr_fibre)

arr_protein = np.asarray(fat)
out_protein = get_outliers(arr_protein)

# Filter data which is lower than outlier value
data = data[data['Fat (g)'] < out_fat]
data = data[data['Carb. (g)'] < out_carb]
data = data[data['Fiber (g)'] < out_fibre]
data = data[data['Protein (g)'] < out_protein]

fat = data['Fat (g)']
carb = data['Carb. (g)']
fibre = data['Fiber (g)']
protein = data['Protein (g)']

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, sharex=True)

ax1.scatter(cal, dv_protein, label='Daily Value percent Protein', s=10, c='green')
ax2.scatter(cal, dv_fibre, label='Daily Value percent Fiber', s=10, c='red')
ax3.scatter(cal, dv_carb, label='Daily Value percent Carb.', s=10, c='blue')
ax4.scatter(cal, dv_fat, label='Daily Value percent Fat', s=10, c='black')

ax1.set_ylabel('% Daily Value Protein')
ax2.set_ylabel('% Daily Value Fiber')
ax3.set_ylabel('% Daily Value Carbohydrates')
ax4.set_ylabel('% Daily Value Fat')

ax1.set_xlabel('Calories')
ax2.set_xlabel('Calories')
ax3.set_xlabel('Calories')
ax4.set_xlabel('Calories')

fig.suptitle('% Daily value of nutrients vs calories of food items at Starbucks')
plt.tight_layout()
plt.show()
