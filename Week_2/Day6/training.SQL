
-- Create database, check it exists and connect to it
CREATE DATABASE skillio;
-- \l
-- \c skillio;

-- Create the table
CREATE TABLE person (
id SERIAL PRIMARY KEY,
name VARCHAR(255) NOT NULL,
age INT NOT NULL,
student BOOLEAN
);

-- Check table was created and add to it
SELECT * FROM person;
INSERT INTO person (name, age, student) VALUES
('Mikko', 25, true), ('Jaana', 31, false), ('Pekka', 21, true);

-- ## Using SQL on the table
--Query only name column
SELECT name FROM person;
-- Query age and id columns.
SELECT age, id FROM person;
-- Query name and id columns in a way that id column shows as ’identifier’ on the results.
SELECT id AS identifier, name FROM person;
-- Query all the columns and order them alphabetically by name column.
SELECT * FROM person ORDER BY name;
	-- Try to also reverse the alphabetical order.
SELECT * FROM person ORDER BY name DESC;
-- Count how many rows there are on the table.
SELECT COUNT(*) FROM person;
-- Count the accumulated age of all rows.
SELECT SUM(age) FROM person;
-- Count the average age of all rows.
SELECT AVG(age) FROM person;

-- Updating the table
UPDATE person SET age = 28 WHERE name = 'Mikko';
UPDATE person SET student = false;

-- Deletion
DELETE FROM person WHERE id = 1