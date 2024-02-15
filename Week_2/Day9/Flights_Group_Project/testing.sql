WITH RankedFlights AS (
	SELECT
		f.departure_airport AS airport_code,
		f.scheduled_departure,
		ROW_NUMBER() OVER (PARTITION BY f.departure_airport ORDER BY f.scheduled_departure DESC) AS row_num
	FROM flights f
)
SELECT
	r.airport_code,
	ad.airport_name,
	r.scheduled_departure AS latest_datetime,
	r.row_num
FROM RankedFlights r
JOIN airports_data ad ON r.airport_code = ad.airport_code
WHERE r.row_num = 1
ORDER BY r.airport_code
LIMIT(200);

-- WITH RankedFlights AS (
--     SELECT
--         f.departure_airport AS airport_code,
--         f.scheduled_departure,
--         ROW_NUMBER() OVER (ORDER BY f.scheduled_departure DESC) AS row_num
--     FROM flights f
-- )
-- SELECT
--     r.airport_code,
--     ad.airport_name,
--     r.scheduled_departure AS latest_datetime,
--     r.row_num
-- FROM RankedFlights r
-- JOIN airports_data ad ON r.airport_code = ad.airport_code
-- WHERE r.row_num = 1
-- ORDER BY r.airport_code
-- LIMIT 200;