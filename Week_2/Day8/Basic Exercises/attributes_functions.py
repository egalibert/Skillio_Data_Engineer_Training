import psycopg2
from config import config
from psycopg2.extras import RealDictCursor
import json

# con = None

def create_attributes_table():
	try:
		con = None
		cursor = None
		con = psycopg2.connect(**config())
		cursor = con.cursor()

		create_table_query = """
			CREATE TABLE attributes (
				id SERIAL PRIMARY KEY,
				attribute_name VARCHAR(50) NOT NULL,
				attribute_description VARCHAR(255),
				attribute_value VARCHAR(50),
				person_id INT,
				CONSTRAINT fk_person FOREIGN KEY (person_id) REFERENCES person (id)
			);
		"""

		cursor.execute(create_table_query)
		con.commit()

		print("Table 'attributes' created successfully.")

	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if cursor is not None:
			cursor.close()

# Example usage
# create_attributes_table()
			
def get_attributes():
	con = None
	try:
		con = psycopg2.connect(**config())
		cursor = con.cursor(cursor_factory=RealDictCursor)
		SQL = 'SELECT * FROM attributes;'
		cursor.execute(SQL)
		data = cursor.fetchall()
		cursor.close()
		return json.dumps({"attributes_list": data})
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if con is not None:
			con.close()

def create_attributes_func(attribute_name, attribute_description, attribute_value, person_id):
	con = None
	try:
		con = psycopg2.connect(**config())
		cursor = con.cursor(cursor_factory=RealDictCursor)
		SQL = 'INSERT INTO attributes (attribute_name, attribute_description, attribute_value, person_id) VALUES (%s, %s, %s, %s);'
		cursor.execute(SQL, (attribute_name, attribute_description, attribute_value, person_id))
		con.commit()
		result = {"success": "created attribute : %s " % attribute_name}
		cursor.close()
		return json.dumps(result)
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if con is not None:
			con.close()

def delete_attributes_func(id):
	con = None
	try:
		con = psycopg2.connect(**config())
		cursor = con.cursor(cursor_factory=RealDictCursor)
		SQL = 'DELETE FROM attributes WHERE id = %s;'
		cursor.execute(SQL, (id,))
		con.commit()
		cursor.close()
		result = {"success": "deleted attribute id: %s " % id}
		return json.dumps(result)
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if con is not None:
			con.close()

def update_attributes_func(id, attribute_name, attribute_description, attribute_value, person_id):
	con = None
	try:
		con = psycopg2.connect(**config())
		cursor = con.cursor(cursor_factory=RealDictCursor)
		SQL = 'UPDATE attributes SET attribute_name = %s, attribute_description = %s, attribute_value = %s, person_id = %s WHERE id = %s;'
		cursor.execute(SQL, (attribute_name, attribute_description, attribute_value, person_id, id))
		con.commit()
		cursor.close()
		result = {"success": "updated attribute id: %s " % id}
		return json.dumps(result)
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if con is not None:
			con.close()