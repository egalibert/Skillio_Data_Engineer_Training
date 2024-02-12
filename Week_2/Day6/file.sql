-- CREATE TABLE certificates (
-- 	id SERIAL PRIMARY KEY,
-- 	name VARCHAR(255) NOT NULL,
-- 	person_id int,
-- 	CONSTRAINT fk_person FOREIGN KEY (person_id) REFERENCES person(id)
-- );

-- INSERT INTO person (name, age, student) VALUES ('Elliot', 28, true);
-- INSERT INTO certificates (name, person_id) VALUES ('Scrum', 5);

-- INSERT INTO certificates (name, person_id) VALUES ('Scrum', 2);
-- INSERT INTO certificates (name, person_id) VALUES ('Azure', 2);
-- INSERT INTO certificates (name, person_id) VALUES ('Scrum', 3);
-- INSERT INTO certificates (name, person_id) VALUES ('Azure', 3);

-- SELECT * FROM person;
-- SELECT * FROM certificates;

SELECT person.*
FROM person
JOIN certificates ON person.id = certificates.person_id
WHERE certificates.name = 'Scrum';

SELECT person.*
FROM person
JOIN certificates ON person.id = certificates.person_id
WHERE certificates.name = 'Azure';

-- EX 9 4.1 
-- CREATE TABLE Customers(
-- 	customer_id int NOT NULL,
-- 	cutomer_name char(50) NOT NULL
-- );

-- CREATE TABLE Orders(
-- 	order_id int NOT NULL,
-- 	customer_id int NOT NULL,
-- 	order_date date NOT NULL,
-- 	CONSTRAINT fk_Customers FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
-- );