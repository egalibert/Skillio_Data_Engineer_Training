import psycopg2
from config import config

con = None
# Query for all the rows in the person table and print them
def all_rows():
	try:
		con = psycopg2.connect(**config())
		cursor = con.cursor()
		SQL = 'SELECT *FROM person;'
		cursor.execute(SQL)
		row = cursor.fetchall()
		print(row)
		cursor.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if con is not None:
			con.close()

# Query for the column names in the person table and print them.
def column_names():
	try:
		con = psycopg2.connect(**config())
		cursor = con.cursor()
		SQL = ("""
		SELECT column_name
		FROM information_schema.columns
		WHERE table_name = 'person';
	""")
		cursor.execute(SQL)
		row = cursor.fetchall()
		print(row)
		cursor.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if con is not None:
			con.close()

# Query for the certificate table column names, as well as the rows, and print them.
def certificate_column_names():
	try:
		con = psycopg2.connect(**config())
		cursor = con.cursor()
		SQL = ("""
		SELECT column_name
		FROM information_schema.columns
		WHERE table_name = 'certificates';
	""")
		SQL2 = ('SELECT * FROM certificates')
		cursor.execute(SQL)
		row = cursor.fetchall()
		print(row)
		cursor.execute(SQL2)
		row2 = cursor.fetchall()
		print(row2)
		cursor.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if con is not None:
			con.close()

# Query person table for average age and print it.
def average_age():
	try:
		con = psycopg2.connect(**config())
		cursor = con.cursor()
		SQL = ("""
		SELECT AVG(age)
		FROM person
	""")
		cursor.execute(SQL)
		row = cursor.fetchone()
		print(row)
		cursor.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if con is not None:
			con.close()

# Query person table for average age and print it.
def average_age():
	try:
		con = psycopg2.connect(**config())
		cursor = con.cursor()
		SQL = ("""
		SELECT AVG(age)
		FROM person
	""")
		cursor.execute(SQL)
		row = cursor.fetchone()
		print(row)
		cursor.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if con is not None:
			con.close()

# Try another query which you did in SQL language earlier (join, group by, subquery...).
def bonus():
	try:
		con = psycopg2.connect(**config())
		cursor = con.cursor()
		SQL = ("""
		SELECT age
		FROM person
		GROUP BY age
		ORDER BY age DESC
	""")
		cursor.execute(SQL)
		row = cursor.fetchall()
		print(row)
		cursor.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if con is not None:
			con.close()

# Add a new row to the certificate table in away that
# the inserted values are taken as function parameters.
def add_certificate(name, person_id):
	try:
		con = psycopg2.connect(**config())
		cursor = con.cursor()
		cursor.execute("""
		INSERT INTO certificates (name, person_id)
		VALUES (%s, %s);
	""", (name, person_id))
		con.commit()
		cursor.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if con is not None:
			con.close()

# Add a new row to the person table by entering values afterwards (Find out why this is
# Best practice and always use this method in the future). Values are taken as function parameters.
			
def add_new_person(name, age, student):
	try:
		con = psycopg2.connect(**config())
		cursor = con.cursor()
		cursor.execute("""
		INSERT INTO person (name, age, student)
		VALUES (%s, %s, %s);
	""", (name, age, student))
		con.commit()
		cursor.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if con is not None:
			con.close()

# Update an existing row in the person table. Values are taken as function parameters.
def update_person(person_id, new_name, new_age, new_student):
	try:
		con = psycopg2.connect(**config())
		cursor = con.cursor()
		cursor.execute("""
			UPDATE person
			SET name = %s, age = %s, student = %s
			WHERE id = %s;
		""", (new_name, new_age, new_student, person_id))
		con.commit()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		cursor.close()

# Update an existing row in the certificate table. Values are taken as function parameters.
def update_certificate(certificate_id, person_id, name):
	try:
		con = psycopg2.connect(**config())
		cursor = con.cursor()
		cursor.execute("""
			UPDATE certificates
			SET name = %s, person_id = %s
			WHERE id = %s;
		""", (name, person_id, certificate_id))
		con.commit()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		cursor.close()

# Remove an existing row from the person table.
# The id of the row to be deleted is taken as a function parameter.
def delete_person(person_id):
	try:
		con = psycopg2.connect(**config())
		cursor = con.cursor()
		cursor.execute("""
			DELETE FROM certificates
			WHERE person_id = %s;
		""", (person_id,))
		cursor.execute("""
			DELETE FROM person
			WHERE id = %s;
		""", (person_id, ))
		con.commit()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		cursor.close()

def delete_certificate(certificate_id):
	try:
		con = psycopg2.connect(**config())
		cursor = con.cursor()
		cursor.execute("""
			DELETE FROM certificates
			WHERE id = %s;
		""", (certificate_id, ))
		con.commit()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		cursor.close()

def create_table(table_name, columns):
	try:
		con = psycopg2.connect(**config())
		cursor = con.cursor()
		create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ("
		for column_name, data_type in columns.items():
			create_table_query += f"{column_name} {data_type}, "
		create_table_query = create_table_query.rstrip(', ') + ");"
		cursor.execute(create_table_query)
		con.commit()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	con.close()


# Make a function that adds an image to the database.
def add_image_to_database(image_path):
	try:
		con = psycopg2.connect(**config())
		cursor = con.cursor()
		with open(image_path, 'rb') as file:
			image_data = file.read()

		cursor.execute("""
			INSERT INTO images (image_data) 
			VALUES (%s)
		""", ((image_data),))

		con.commit()
		print("Image added to the database.")

	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()

# Make a function that retrieves an image from the database.
def retrieve_image_from_database(image_id, save_path):
	try:
		con = psycopg2.connect(**config())
		cursor = con.cursor()
		cursor.execute("""
			SELECT image_data FROM images
			WHERE id = %s
		""", (image_id,))

		image_data = cursor.fetchone()[0]
		with open(save_path, 'wb') as file:
			file.write(image_data)
		print(f"Image retrieved and saved to {save_path}.")

	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()





def main():

	# column_names()
	# certificate_column_names()
	# average_age()
	# bonus()
	# add_certificate('AWS', 2)
	# add_new_person('Jaakko', 21, True)
	# update_person(2, 'Sirkka', 30, False)
	# update_certificate(2, 3, 'Hello World',)
	# delete_person(2)
	# delete_certificate(1)

	# new_table_columns = {
	# 'id': 'SERIAL PRIMARY KEY',
	# 'name': 'VARCHAR(255)',
	# 'work_years': 'INT',
	# 'role': 'VARCHAR(255)'
	# }
	# create_table('Employers', new_table_columns)
	# all_rows()

	# add_image_to_database("image_path")
	# retrieve_image_from_database("image_path")

	while(1):
		print("Welcome to person database editor!")
		choice = input("Choose what action you want to perform (ADD, UPDATE, DELETE, C_NAMES, PRINT_ALL, AVG_AGE, EXIT): ")
		if choice == "ADD":
			name = input("Give a name: ")
			age = input("Give an age: ")
			student = input("Is the person a student(True/False): ")
			if student == 'True':
				student = True
			else:
				student = False
			add_new_person(name, age, student)
		elif choice == "UPDATE":
			name = input("Give a name: ")
			age = input("Give an age: ")
			student = input("Is the person a student(True/False): ")
			if student == 'True':
				student = True
			else:
				student = False
			update_person(name, age, student)
		elif choice == "DELETE":
			id = input("Give the id of the person you want to delete: ")
			delete_person(id)
		elif choice == "C_NAMES":
			column_names()
		elif choice == "PRINT_ALL":
			all_rows()
		elif choice == "AVG_AGE":
			average_age()
		elif choice == "EXIT":
			break
		else:
			print("You chose an invalid command, try again")
			continue
		

main()