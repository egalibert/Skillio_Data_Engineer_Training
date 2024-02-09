import pandas as pd
file = "Data.csv"

df = pd.read_csv(file)
cleaned_df = df[['Category', 'Material', 'Price']]
cleaned_df = cleaned_df.dropna()

final_df = cleaned_df.groupby(['Category', 'Material']).agg({'Price': 'mean'}).reset_index()

# Rename the calculated column
final_df.rename(columns={'Price': 'AveragePrice'}, inplace=True)
final_df = final_df.drop(index=8)
final_df = final_df.reset_index(drop=True)
final_df['Category'] = final_df['Category'].str.replace(' ', '').str.replace('&', '')

# print(cleaned_df)
print(final_df)