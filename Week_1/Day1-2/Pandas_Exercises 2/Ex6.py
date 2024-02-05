import pandas as pd

df = pd.read_csv('titanic.csv')

male_df = df[df['Sex'] == 'male']

female_df = df[df['Sex'] == 'female']

child_df = df[df['Age'] < 18]

print(f"Male df has = {male_df.shape}")
print(f"Female df has = {female_df.shape}")
print(f"Child df has = {child_df.shape}")