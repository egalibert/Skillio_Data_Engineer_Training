-- # Login to postgres and create database from terminal \c exam
-- CREATE DATABASE exam;

-- Switched to VScode and created connection using SQLTools
-- BASIC PART
CREATE TABLE flights (
	id SERIAL PRIMARY KEY,
	flight_number VARCHAR(255),
	departure_time TIMESTAMP,
	arrival_time TIMESTAMP,
	departure_airport VARCHAR(255),
	destination_airport VARCHAR(255)
);

INSERT INTO flights (flight_number, departure_time, arrival_time, departure_airport, destination_airport)
VALUES
	('AY217', '2024-02-16 10:00:00', '2024-02-16 20:00:00', 'Helsinki', 'Bangkok'),
	('BA681', '2024-02-17 14:30:00', '2024-02-17 16:30:00', 'London', 'Liverpool'),
	('AY518', '2024-02-18 08:45:00', '2024-02-18 19:45:00', 'Bangkok', 'Helsinki');

-- EXTRA

CREATE TABLE airline (
	id SERIAL PRIMARY KEY,
	name VARCHAR(255),
	flights_id INT,
	FOREIGN KEY (flights_id) REFERENCES flights(id)
);

INSERT INTO airline (name, flights_id) VALUES
	('Finnair', 1),
	('British Airways', 2),
	('Finnair', 3),
	('Finnair', 4),
	('Finnair', 5),
	('Finnair', 6);