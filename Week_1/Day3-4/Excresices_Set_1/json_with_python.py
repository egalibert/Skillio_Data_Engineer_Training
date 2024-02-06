import json

item = {
	"name" : "Book of knowledge",
	"rarity" : "common",
	"durability" : 100
}

print(item)
itemJson = json.dumps(item)
print(itemJson)
new_dict = json.loads(itemJson)
print(new_dict)

with open("test.json", "w") as file:
	file.write(itemJson)

with open('sample.json', 'r') as openfile:
	json_object = json.load(openfile)

print(json_object)