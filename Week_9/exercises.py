
import requests
import json
from azure.cosmos import CosmosClient
from azure.cosmos import exceptions


ENDPOINT = ''
KEY = ''

URL = 'https://dummyjson.com/products/'
api_result = requests.get(url=URL)
data = api_result.json()

# for prodcut in data['products']:
# 	print(prodcut['title'])

cosmos_client = CosmosClient(ENDPOINT, KEY)
database_name = 'ToDoList'
container_name = 'items2'

# def update_partition_keys(endpoint, key, database_name, container_name, start_id=1, end_id=30):
# 	# Initialize Cosmos DB client
# 	cosmos_client = CosmosClient(endpoint, key)

# 	# Get a reference to the database and container
# 	database = cosmos_client.get_database_client(database_name)
# 	container = database.get_container_client(container_name)

# 	# Loop through IDs from start_id to end_id
# 	for i in range(start_id, end_id + 1):
# 		# Construct the document ID
# 		item_id = str(i)

# 		# Read the document from the container
# 		try:
# 			item = container.read_item(item=item_id)

# 			# Update the document with the partition key value
# 			item['partitionKey'] = str(i)

# 			# Replace the existing document with the updated version
# 			container.replace_item(item=item, body=item)

# 			print(f"Document with ID {item_id} updated successfully.")
# 		except Exception as e:
# 			print(f"Error updating document with ID {item_id}: {e}")

def create():
	for item in data['products']:

		item['id'] = str(item['id'])
		item_json = json.dumps(item)

		database = cosmos_client.get_database_client(database_name)
		container = database.get_container_client(container_name)
		# CRUD!
		# C = Create
		container.create_item(body=json.loads(item_json))

# R = Read
def read():
	database = cosmos_client.get_database_client(database_name)
	container = database.get_container_client(container_name)

	query = 'SELECT * FROM c'
	items = list(container.query_items(query=query, enable_cross_partition_query=True))
	for item in items:
		print(item)

# U = Update
def update(item_id, new_price):
	database = cosmos_client.get_database_client(database_name)
	container = database.get_container_client(container_name)

	item_to_update = container.read_item(item=item_id, partition_key=item_id)	
	# Update the price
	item_to_update['price'] = new_price

	# Replace the document in the container with the updated version
	container.replace_item(item=item_to_update, body=item_to_update)


# D = Delete
def delete():
	database = cosmos_client.get_database_client(database_name)
	container = database.get_container_client(container_name)

	item_to_delete = container.read_item(item='item_id', partition_key='partitionKey')
	container.delete_item(item=item_to_delete['id'], partition_key='partitionKkey')

def main():
	# read()
	# update_partition_keys(ENDPOINT, KEY, database_name, container_name)
	update('1', 12345)

if __name__ == "__main__":
	main()