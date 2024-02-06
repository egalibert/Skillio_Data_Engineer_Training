# Exercise: eCommerce Sales Data Analysis
# Objective:
# Analyze an eCommerce dataset to practice data ingestion, cleaning, manipulation, and transformation skills using pandas.
# Dataset:
# A hypothetical ecommerce_sales.csv file with columns: order_id, product_id,
# product_category, quantity, unit_price, customer_id, order_date, and country.
# Part 1: Data Ingestion

# Task 1.1: Load the dataset into a pandas DataFrame and display the first ten rows.
#Explore the basic information about the dataset (size, shape, data types).
# Part 2: Data Cleaning

# Task 2.1: Identify and handle missing values in the dataset.
# Options include dropping, filling with a placeholder, or imputing based on other data points.
# Task 2.2: Ensure all data types are correct, focusing on converting order_date to a
# datetime format and checking numerical columns for consistency.
# Part 3: Data Manipulation

# Task 3.1: Create a new column total_price that represents the total amount
# spent on each order (calculated as quantity * unit_price).
# Task 3.2: Extract additional features from the order_date column,
# such as order_weekday (the day of the week), and order_month (month of the year).
# Part 4: Data Transformation

# Task 4.1: Group the data by product_category and summarize the total sales and average quantity sold in each category.
# Task 4.2: Pivot the data to create a summary table showing total sales per month for each product category.
# Task 4.3: Normalize the unit_price column to show prices as a percentage of the average price across all products.

import pandas as pd
import datetime

# Task 1
df = pd.read_csv("bonus.csv")
print(df.head(10))
# print(df.dtypes)
# print(df.describe(), df.shape)

# Task2.1
# print(df.isna())
values = {"customer_id" : 509, "country" : "USA", "unit_price" : df["unit_price"].mean()}
df = df.fillna(value=values)
df = df.dropna()
print(df.isna())

# Task2.2
# print(df.dtypes)
df["order_date"] = pd.to_datetime(df["order_date"])
print(df.dtypes)

# Task 3.1
df["total_price"] = df["quantity"] * df["unit_price"]
print(df.head(10))

# Task 3.2
df["order_weekday"] = df["order_date"]