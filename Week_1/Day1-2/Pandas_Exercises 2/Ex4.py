# 4. Crete a new dataset which displays the average fare per sex and Pclass

import pandas as pd

df = pd.read_csv('titanic.csv')

new_df = df.groupby(['Sex', 'Pclass'])['Fare'].mean()
print(new_df)