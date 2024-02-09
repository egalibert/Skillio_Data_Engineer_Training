import pandas as pd
file = "Data.csv"

df = pd.read_csv(file)
cleaned_df = df[['Category', 'Material', 'Price']]
cleaned_df = cleaned_df.dropna()

average_price_df = cleaned_df.groupby(['Category', 'Material']).agg({'Price': 'mean'}).reset_index()

# Rename the calculated column
average_price_df.rename(columns={'Price': 'AveragePrice'}, inplace=True)
average_price_df = average_price_df.drop(index=8)
average_price_df = average_price_df.reset_index(drop=True)

# print(cleaned_df)
print(average_price_df)