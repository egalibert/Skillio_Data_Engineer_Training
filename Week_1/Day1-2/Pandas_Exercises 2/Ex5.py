# 5. Create a new dataset which displays the average fare per survived column

import pandas as pd

df = pd.read_csv('titanic.csv')

new_df = df.groupby('Survived')['Fare'].mean()
print(new_df)