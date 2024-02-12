-- Query the city table for all rows with country_codeFIN.
	-- -Arrange the result alphabetically by name.

SELECT * FROM city
WHERE country_code = 'FIN'
ORDER BY name;

-- Count how many cities can be found in the United States.
SELECT COUNT(*) FROM city
WHERE country_code = 'USA'

-- Count the population of U.S. cities.
SELECT SUM(population) FROM city
WHERE country_code = 'USA'

-- List cities with populations between 1 and 2 million
	-- -Limit search result to 15 rows.
SELECT * FROM city
WHERE population > 1000000 and population < 2000000
LIMIT(15)

-- Calculate the total population of cities in U.S. states, grouped by state.
SELECT SUM(population) FROM city
WHERE country_code = 'USA'
GROUP BY district

-- Calculate which country has the highest lifeexpectancy.
	-- -Null values are not included.
	-- -Limit search result to one row.

SELECT name, lifeexpectancy FROM country
WHERE lifeexpectancy IS NOT NULL
ORDER BY lifeexpectancy DESC
LIMIT 1

-- Calculate the total number of inhabitants in all cities in a given country grouped by country.
-- Include relevant columns in the search result.
-- 	-Next, include the population column from the country table. The numbers should not add up

SELECT 
	country.name,
	country.continent,
	country.region,
	country.surfacearea,
	country.indep_year,
	country.population AS country_population,
	(
		SELECT SUM(city.population) 
		FROM city 
		WHERE city.country_code = country.code
	) AS total_city_population
FROM 
	country
ORDER BY 
	country.name;

-- ## USING JOIN
-- List countries by capital, use the JOIN clause.SELECT country.name, country.capital, city.name
SELECT country.name, country.capital, city.name
FROM country
JOIN city on country.capital = city.id;

-- List Spain only.
SELECT country.name, country.capital, city.name
FROM country
JOIN city on country.capital = city.id
WHERE country.name = 'Spain';

-- List all European countries and their cities.
SELECT country.name, country.capital, city.name
FROM country
JOIN city on country.capital = city.id
WHERE country.continent = 'Europe';

-- List all languages spoken in Southeast Asia region, use the join clause.
SELECT country.name, country.SELECT 
	cl.language,
	c.name AS country_name,
	c.region
FROM 
	country.language cl
JOIN 
	country c ON cl.countrycode = c.code
WHERE 
	c.region = 'Southeast Asia';

-- ## USING SUBQUERIES
-- Use the subquery and search for all cities with a larger population than the entire population of Finland.
SELECT name AS city_name, population
FROM city
WHERE population > (SELECT population FROM country WHERE name = 'Finland');

-- Search all cities with over one million inhabitants in a country where English is spoken.
SELECT city.name AS city_name, city.population
FROM city
JOIN countrylanguage ON city.countrycode = country.language.countrycode
WHERE city.population > 1000000
  AND countrylanguage.language = 'English';
