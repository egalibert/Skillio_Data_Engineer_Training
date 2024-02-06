# 7. Create a new dataset that only includes Pclass, Name and age,
# for those persons that had siblings, spouces, parents or children aboard

import pandas as pd

df = pd.read_csv('titanic.csv')
new_df = df.loc[(df['Siblings/Spouses Aboard'] > 0) | (df['Parents/Children Aboard'] > 0), ['Pclass', 'Name', 'Age']]

print(new_df)