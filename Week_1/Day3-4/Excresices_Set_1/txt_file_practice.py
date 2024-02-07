word_list = []

with open("story.txt", "r") as file:
	for line in file:
		word_list += line.split(" ")

for word in word_list:
	print(word)

sorted_list = sorted(word_list, key=len, reverse=True) #False to make shortest to longest
print(sorted_list)

with open("sortedWords.txt", "w") as file:
	for word in sorted_list:
		file.write(word)
		file.write(" ")