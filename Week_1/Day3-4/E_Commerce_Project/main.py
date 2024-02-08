# Objective: Construct and manipulate a simulated e-commerce transactions dataset
# to practice data wrangling techniques using Pandas and NumPy.
# The exercise will involve generating synthetic data, handling data in JSON format,x
# and performing various data wrangling tasks.

# Part 1: Data generation
# 1. User data generation
# Generate a synthetic dataset of users with the following details:
# user ID, name, email, and signup date. Use NumPy for generating user IDs and signup dates, and any method for fake name and email generation.

# 2. Product catalogue
# Create a product catalogue with product ID, product name, category, and price. You can manually create this dataset or generate it synthetically.

# 3. Transactions data
# Simulate transaction data that includes transaction ID, user ID, product ID, quantity, and transaction date.
# Ensure the transaction dates and quantities are randomly generated to simulate real purchase behavior.

# Part 2: Data wrangling
# 1. Loading data
# Start by loading your generated datasets into Pandas DataFrames.

# 2. Data cleaning
# Ensure all datasets are clean. This includes handling missing values, removing duplicates, and ensuring data types are appropriate for each column.

# 3. Merging datasets
# Merge the user data with transactions to create a comprehensive dataset that shows which user bought what product.
# Also, merge the product catalogue with the transactions to include product details in the transactions dataset.

# 4. Aggregation tasks
# Calculate the total spending per user.
# Find the top 5 best-selling products and their average price.
# Determine the most popular product category.

# 5. Exporting as JSON
# Export the merged and cleaned transactions dataset to a JSON file.
# Explore how different 'orient' parameter options affect the output file
# Demonstrate how to read this JSON file back into a Pandas DataFrame.

import numpy as np
from faker import Faker
import pandas as pd
from datetime import datetime, timedelta
import random
import json

## USER DATA ##
# Set seed for reproducibility
np.random.seed(42)

# Number of users in the dataset
num_users = 20

# Generate user IDs
user_ids = np.arange(1, num_users + 1)

# Generate fake names and emails
fake = Faker()
names = [fake.name() for _ in range(num_users)]
emails = [fake.email() for _ in range(num_users)]

# Generate random signup dates within the last year
end_date = datetime.now()
start_date = end_date - timedelta(days=365)
signup_dates = [fake.date_time_between_dates(start_date, end_date) for _ in range(num_users)]

# Create a DataFrame with the generated data
user_data = {
	'user_id': user_ids,
	'name': names,
	'email': emails,
	'signup_date': signup_dates
}

user_df = pd.DataFrame(user_data)
print(user_df)

# Display the synthetic dataset
## PRODUCT DATA ##

product_data = {
	'product_id': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009],
	'Product Name': ['Smartphone', 'Laptop', 'Headphones', 'Running Shoes', 'Blender', 'Basketball', 'Bat', 'Coffee maker', 'Spoon'],
	'Category': ['Electronics', 'Electronics', 'Electronics', 'Sports', 'Kitchen', 'Sports', 'Sports', 'Kitchen','Kitchen' ],
	'Price': [699.99, 999.99, 149.99, 79.99, 49.99, 29.99, 99.99, 44.99, 2.99]
}

# Create a product DataFrame
product_df = pd.DataFrame(product_data)
# print(product_df)

## TRANSACTION DATA ##
# Number of transactions
num_transactions = 100

# User data (assuming you already have the DataFrame df from the previous example)
user_ids = user_df['user_id'].sample(num_transactions, replace=True).values

# Product data
product_ids = product_df['product_id'].sample(num_transactions, replace=True).values

# Generate fake transaction IDs
transaction_ids = np.arange(1, num_transactions + 1)

# Generate random quantities
quantities = np.random.randint(1, 10, size=num_transactions)

# Generate random transaction dates within the last year
end_date = datetime.now()
start_date = end_date - timedelta(days=365)
transaction_dates = [fake.date_time_between_dates(start_date, end_date) for _ in range(num_transactions)]

# Create a DataFrame with the generated transaction data
transaction_data = {
	'transaction_id': transaction_ids,
	'user_id': user_ids,
	'product_id': product_ids,
	'quantity': quantities,
	'transaction_date': transaction_dates
}

transaction_df = pd.DataFrame(transaction_data)
# print(transaction_df)

## MERGE DATA ##

transaction_and_users = pd.merge(user_df, transaction_df, on = "user_id")
# print(transaction_and_users)
# print(transaction_and_users.columns)

all_data = pd.merge(transaction_and_users, product_df, on = "product_id")
all_data["transaction_val"] = all_data["quantity"] * all_data["Price"]

print(all_data)
# print(all_data.columns)

total_spending = all_data.groupby('user_id').sum("transaction_val")
print(total_spending)

topsellers = all_data.groupby('Product Name').sum("quantity")
sorted_topsellers = topsellers.sort_values('quantity', ascending=False).loc[:,['quantity']]
sorted_topsellers = sorted_topsellers.reset_index()

# print(sorted_topsellers)

st_wprice = pd.merge(sorted_topsellers, product_df, on="Product Name")
mean_price = st_wprice.loc[0:4,['Price']].mean()

# print(st_wprice)
print(mean_price)

most_popular = all_data.groupby('Category').sum("quantity").sort_values('quantity', ascending=False)
print(most_popular)

json_data1 = all_data.to_json(orient='index')
json_data2 = all_data.to_json(orient='columns')
json_data3 = all_data.to_json(orient='values')
json_data4 = all_data.to_json(orient='records')

#print(json_data1)
# print(json_data2)
# print(json_data3)
# print(json_data4)

with open("transactions.json", 'w') as json_file:
	json.dump(json_data4, json_file)


with open("transactions.json") as f:
	data = json.load(f)
output_df = pd.read_json(data)

print(output_df)