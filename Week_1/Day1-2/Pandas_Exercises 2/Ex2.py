import pandas as pd

df = pd.read_csv('titanic.csv')

# df['Child'] = df[df['Age'] < 18]
df['Child'] = df['Sex'].apply(lambda x: 'Child' if df['Age'] < 18 else 'Sex')

print(df.columns)

