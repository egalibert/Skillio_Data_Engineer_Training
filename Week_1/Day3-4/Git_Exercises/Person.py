class Person:
	def __init__(self):
		self.name = "Luffy"
		self.age = 19

	def get_name_and_age(self):
		return (self.name, self.age)
	
	def set_name_and_age(self, name, age):
		self.name = name
		self.age = age
		return (self.name, self.age)
	
	def __str__(self) -> str:
		print(f"This person is called{self.name}, and is {self.age} years old")