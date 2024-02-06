# 1. Rename columns not to have any whitespaces or special characters.

import pandas as pd

df = pd.read_csv('titanic.csv')

print(df.columns)
df = df.rename(columns={'Siblings/Spouses Aboard' : 'SiblingsSpousesAboard', 'Parents/Children Aboard' : 'ParentsChildrenAboard'})
print(df.columns)