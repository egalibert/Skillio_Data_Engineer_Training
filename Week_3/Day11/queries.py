import psycopg2
from config import config
from datetime import datetime

con = None

def all_rows():
	try:
		con = psycopg2.connect(**config())
		cursor = con.cursor()
		SQL = 'SELECT * FROM person;'
		cursor.execute(SQL)
		row = cursor.fetchall()
		print(row)
		cursor.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if con is not None:
			con.close()

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


def main():
	all_rows()
	add_new_person('Sami', 67, False)
	all_rows()


main()