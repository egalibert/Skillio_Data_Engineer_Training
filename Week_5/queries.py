from config import config
import psycopg2
from datetime import date

def all_rows():
	try:
		con = psycopg2.connect(**config())
		cursor = con.cursor()
		SQL = 'SELECT *FROM Customers;'
		cursor.execute(SQL)
		row = cursor.fetchall()
		print(row)
		cursor.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if con is not None:
			con.close()

def add_customers(customers_data):
	try:
		con = psycopg2.connect(**config())
		cursor = con.cursor()
		cursor.executemany("INSERT INTO Customers (Customer_id, Name, Review_id, Order_id) VALUES (%s, %s, %s, %s)",
			customers_data)
		con.commit()
		cursor.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if con is not None:
			con.close()

def add_products(products_data):
	try:
		con = psycopg2.connect(**config())
		cursor = con.cursor()
		cursor.executemany("INSERT INTO Product (Product_id, Quantity_in_stock, Product_name, Price) VALUES (%s, %s, %s, %s)",
				products_data)
		con.commit()
		cursor.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if con is not None:
			con.close()

def add_orders(orders_data):
	try:
		con = psycopg2.connect(**config())
		cursor = con.cursor()
		cursor.executemany("INSERT INTO Orders (Order_id, Order_date, Delivered, Total_amount, Product_id) VALUES (%s, %s, %s, %s, %s)",
				orders_data)
		con.commit()
		cursor.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if con is not None:
			con.close()

def add_reviews(reviews_data):
	try:
		con = psycopg2.connect(**config())
		cursor = con.cursor()
		cursor.executemany("INSERT INTO Reviews (Review_id, Rating, Product_id) VALUES (%s, %s, %s)",
			reviews_data)
		con.commit()
		cursor.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if con is not None:
			con.close()

def find_top_selling_products():
	try:
		conn = psycopg2.connect(**config())
		cursor = conn.cursor()

		query = """
		SELECT
			p.Product_id,
			p.Product_name,
			COUNT(o.Order_id) AS total_sold_count
		FROM
			Product p
		LEFT JOIN
			Orders o ON p.Product_id = o.Product_id
		GROUP BY
			p.Product_id, p.Product_name
		ORDER BY
			total_sold_count DESC;
		"""

		cursor.execute(query)
		top_selling_products = cursor.fetchall()

		return top_selling_products

	except (Exception, psycopg2.DatabaseError) as error:
		print(error)

	finally:
		if conn is not None:
			conn.close()

def calculate_inventory_levels():
	try:
		conn = psycopg2.connect(**config())
		cursor = conn.cursor()

		query = """
		SELECT
			p.Product_id,
			p.Product_name,
			p.Quantity_in_stock - COALESCE(COUNT(o.Order_id), 0) AS inventory_level
		FROM
			Product p
		LEFT JOIN
			Orders o ON p.Product_id = o.Product_id
		GROUP BY
			p.Product_id, p.Product_name, p.Quantity_in_stock
		ORDER BY
			inventory_level DESC;
		"""

		cursor.execute(query)
		inventory_levels = cursor.fetchall()

		return inventory_levels

	except (Exception, psycopg2.DatabaseError) as error:
		print(error)

	finally:
		if conn is not None:
			conn.close()

def find_most_valuable_customers():
	try:
		conn = psycopg2.connect(**config())
		cursor = conn.cursor()

		query = """
		SELECT
			c.Customer_id,
			c.Name,
			SUM(o.Total_amount) AS total_spent
		FROM
			Customers c
		LEFT JOIN
			Orders o ON c.Order_id = o.Order_id
		GROUP BY
			c.Customer_id, c.Name
		ORDER BY
			total_spent DESC;
		"""

		cursor.execute(query)
		most_valuable_customers = cursor.fetchall()

		return most_valuable_customers

	except (Exception, psycopg2.DatabaseError) as error:
		print(error)

	finally:
		if conn is not None:
			conn.close()
			
def add_customer_loyalty_levels():
	try:
		conn = psycopg2.connect(**config())
		cursor = conn.cursor()

		# Calculate total spend for each customer
		query = """
		SELECT
			c.Customer_id,
			c.Name,
			COALESCE(SUM(o.Total_amount), 0) AS total_spend
		FROM
			Customers c
		LEFT JOIN
			Orders o ON c.Order_id = o.Order_id
		GROUP BY
			c.Customer_id, c.Name;
		"""
		cursor.execute(query)
		customers_total_spend = cursor.fetchall()

		# Determine loyalty level and insert into CustomerLoyaltyLevels
		for customer in customers_total_spend:
			loyalty_level = determine_loyalty_level(customer[2])
			
			# Insert into CustomerLoyaltyLevels
			insert_query = """
			INSERT INTO CustomerLoyaltyLevels (Customer_id, LoyaltyLevel, StartDate, EndDate)
			VALUES (%s, %s, %s, %s);
			"""
			cursor.execute(insert_query, (customer[0], loyalty_level, date.today(), None))
			print(f"Inserted loyalty level '{loyalty_level}' for customer {customer[0]} ({customer[1]})")

			update_query = """
			UPDATE Customers
			SET LoyaltyLevel_id = (
				SELECT LoyaltyLevel_id
				FROM CustomerLoyaltyLevels
				WHERE Customer_id = %s AND EndDate IS NULL
				ORDER BY StartDate DESC
				LIMIT 1
			)
			WHERE Customer_id = %s;
			"""
			cursor.execute(update_query, (customer[0], customer[0]))

		conn.commit()

	except (Exception, psycopg2.DatabaseError) as error:
		print(f"Error: {error}")
		conn.rollback()

	finally:
		if conn is not None:
			conn.close()

def determine_loyalty_level(total_spend):
	if total_spend < 500:
		return 'Bronze'
	elif 500 <= total_spend < 1000:
		return 'Silver'
	elif 1000 <= total_spend < 5000:
		return 'Gold'
	else:
		return 'Platinum'

def main():
	customers_data = [
	(1, 'Jaakko Kervinen', 1, 101),
	(2, 'Simo Pöllönen', 2, 102),
	(3, 'Timo Koivu', 3, 103),
	(4, 'Aliisa Ruska', 4, 104),
	(5, 'Heikki Tahvanainen', 5, 105)
]
	
	products_data = [
	(1, 100, 'Football', 79.00),
	(2, 50, 'Football boots', 299.00),
	(3, 200, 'Ice hockey stick', 120.00),
	(4, 75, 'Shorts', 29.00),
	(5, 150, 'Snowboard', 200.00)
]
	
	orders_data = [
	(101, '2024-03-04', True, 1200.00, 1),
	(102, '2024-03-05', True, 500.00, 2),
	(103, '2024-03-06', True, 150.00, 3),
	(104, '2024-03-07', True, 600.00, 4),
	(105, '2024-03-08', False, 100.00, 5)
]
	
	reviews_data = [
	(1, 4.5, 1),
	(2, 5.0, 2),
	(3, 3.5, 3),
	(4, 4.0, 4),
	(5, 2.5, 5)
]
	
	# add_customers(customers_data)
	# add_orders(orders_data)
	# add_products(products_data)
	# add_reviews(reviews_data)
	# all_rows()

	# # Finding top selling products
	# top_selling_products = find_top_selling_products()
	# for product in top_selling_products:
	# 	print(f"Product ID: {product[0]}, Product Name: {product[1]}, Total Quantity Sold: {product[2]}")

	# # Checking inverntoey levels
	# inventory_levels = calculate_inventory_levels()
	# for product in inventory_levels:
	# 	print(f"Product ID: {product[0]}, Product Name: {product[1]}, Inventory Level: {product[2]} products left")

	# # Calculating most valuable customer
	# most_valuable_customers = find_most_valuable_customers()
	# for customer in most_valuable_customers:
	# 	print(f"Customer ID: {customer[0]}, Customer Name: {customer[1]}, Total Spent: {customer[2]}")

	add_customer_loyalty_levels()

# Exercise 2, Our model is almost normalized,
	# Denormalized version CREATE TABLE DenormalizedTable
	# (
	#   Customer_id INT NOT NULL,
	#   Customer_name VARCHAR(50) NOT NULL,
	#   Customer_review_id INT NOT NULL,
	#   Customer_order_id INT NOT NULL,
	#   Order_id INT NOT NULL,
	#   Order_date DATE NOT NULL,
	#   Order_delivered BOOLEAN NOT NULL,
	#   Order_total_amount FLOAT NOT NULL,
	#   Product_id INT NOT NULL,
	#   Product_quantity_in_stock INT NOT NULL,
	#   Product_name VARCHAR(100) NOT NULL,
	#   Product_price FLOAT NOT NULL,
	#   Review_id INT NOT NULL,
	#   Review_rating FLOAT NOT NULL,
	#   PRIMARY KEY (Customer_id)
	# );
		
		# Conclusion:

		# Denormalizing your tables into a single flat table simplifies certain queries
		# and might improve performance for specific use cases. However,
		# it comes at the cost of increased redundancy, potential data integrity issues,
		# and reduced flexibility in adapting to changing requirements.
		# The decision to denormalize should be made carefully, 
		# considering the specific needs of your application and the balance between simplicity and long-term maintainability.



if __name__ == '__main__':
	main()