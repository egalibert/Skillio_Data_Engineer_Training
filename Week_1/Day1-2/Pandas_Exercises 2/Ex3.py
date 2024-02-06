# 3. Create a new dataset which displays the average fare per sex

import pandas as pd

df = pd.read_csv('titanic.csv')

new_df = df.groupby('Sex')['Fare'].mean()
print(new_df)
