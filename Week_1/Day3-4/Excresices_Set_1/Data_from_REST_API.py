import requests
import json

URL = "https://api.github.com/search/repositories?q=language:python"

response = requests.get(url=URL)
response.raise_for_status()
data = json.loads(response.text)

for repo in data['items']:
	forks = repo.get('forks', 'N/A')
	name = repo.get('name', 'N/A')
	description = repo.get('description', 'N/A')

	print(f"Forks:{forks}. Name:{name}. Description:{description}")