# 2. For every person under the age of 18, set "sex" column value to be "child"

import pandas as pd

df = pd.read_csv('titanic.csv')

# df['Child'] = df[df['Age'] < 18]
df['Sex'] = df.apply(lambda row: 'Child' if row['Age'] < 18 else row['Sex'], axis=1)

print(df['Sex'])

