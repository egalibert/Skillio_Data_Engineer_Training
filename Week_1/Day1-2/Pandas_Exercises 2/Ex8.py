import pandas as pd

df = pd.read_csv('titanic.csv')

# print(df)
new_df = df[(df['Siblings/Spouses Aboard'] == 0) & (df['Parents/Children Aboard'] == 0)]

print(new_df)
