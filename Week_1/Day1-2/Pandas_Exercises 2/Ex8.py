import pandas as pd

df = pd.read_csv('titanic.csv')
new_df = df.loc[(df['Siblings/Spouses Aboard'] > 0) & (df['Parents/Children Aboard'] > 0)].drop()

print(new_df)
