import requests

URL = "https://catfact.ninja/fact"
new_list = []

for i in range(5):
	response = requests.get(url=URL)
	response.raise_for_status()
	data = response.json()
	new_list.append(data)

# print(new_list)
for item in new_list:
	print(item)