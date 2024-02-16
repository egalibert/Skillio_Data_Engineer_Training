import psycopg2
from config import config
from datetime import datetime

con = None

def all_rows():
	try:
		con = psycopg2.connect(**config())
		cursor = con.cursor()
		SQL = 'SELECT * FROM flights;'
		cursor.execute(SQL)
		row = cursor.fetchall()
		print(row)
		cursor.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if con is not None:
			con.close()

######### EX5
def add_new_flight(flight_number, departure_time, arrival_time, departure_airport, destination_airport):
	try:
		con = psycopg2.connect(**config())
		cursor = con.cursor()
		cursor.execute("""
		INSERT INTO flights (flight_number, departure_time, arrival_time, departure_airport, destination_airport)
		VALUES (%s, %s, %s, %s, %s);
	""", (flight_number, departure_time, arrival_time, departure_airport, destination_airport))
		con.commit()
		cursor.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if con is not None:
			con.close()

######## EX6
def all_rows_departure_time():
	try:
		con = psycopg2.connect(**config())
		cursor = con.cursor()
		SQL = 'SELECT * FROM flights ORDER BY departure_time;'
		cursor.execute(SQL)
		row = cursor.fetchall()
		print(row)
		cursor.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if con is not None:
			con.close()

def all_flights_by_airline_name():
	try:
		con = psycopg2.connect(**config())
		cursor = con.cursor()
		SQL = """
			SELECT flights.id, flights.flight_number, flights.departure_time, flights.arrival_time,
					flights.departure_airport, flights.destination_airport, airline.name AS airline_name
			FROM flights
			JOIN airline ON flights.id = airline.flights_id
			ORDER BY airline.name;
	"""
		cursor.execute(SQL)
		row = cursor.fetchall()
		print(row)
		cursor.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if con is not None:
			con.close()

def delete_information(flight_id):
	con = psycopg2.connect(**config())
	cursor = con.cursor()

	try:
		cursor.execute("""
			DELETE FROM airline
			WHERE flights_id = %s;
		""", (flight_id,))
		cursor.execute("""
			DELETE FROM flights
			WHERE id = %s;
		""", (flight_id,))
		con.commit()

		print(f"Flight with id {flight_id} and associated airline rows removed successfully.")
	except Exception as e:
		con.rollback()
		print(f"Error: {e}")
	finally:
		# cursor.commit()
		cursor.close()
		con.close()


def main():
	# EX 4 print all rows so connection worked
	# all_rows()
	
	# EX 5 three added rows
	# add_new_flight('AY612', datetime(2024, 2, 15, 10, 00), datetime(2024, 2, 15, 10, 0), 'Helsinki', 'Rovaniemi')
	# add_new_flight('AY717', datetime(2024, 2, 17, 14, 30), datetime(2024, 2, 17, 16, 30), 'Rovaniemi', 'Helsinki')
	# add_new_flight('AY891', datetime(2024, 2, 18, 8, 45), datetime(2024, 2, 18, 19, 45), 'Helsinki', 'Singapore')

	# EX 6 print by departure time
	all_rows_departure_time()

	# EX 9 print by airline names in alphabetical order
	# all_flights_by_airline_name()

	# EX 10 delete one row
	# delete_information(6)
	# all_flights_by_airline_name()

main()