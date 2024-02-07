import json

item = {
	"name" : "Book of knowledge",
	"rarity" : "common",
	"durability" : 100
}

item["description"] = {
	"text": "This is a book of knowledge",
	"author": "Unknown",
	"importantPages": [33, 44, 555]
}

item['price'] = 1000
item.update({'sellers':["John", "Peter", "Mary"]})


print(item)
print(item["price"])
print(item["sellers"][1])
print(item["description"]["importantPages"][2])
print(f"Description: {item['description']['text']}\nBookmarked page: {item['description']['importantPages'][2]}")