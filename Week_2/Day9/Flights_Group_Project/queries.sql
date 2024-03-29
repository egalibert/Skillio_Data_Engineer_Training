-- SELECT	
-- 		f.flight_id,
-- 		f.arrival_airport,
-- 		sq.seat_count,
-- 		SUM(sq.seat_count) OVER (PARTITION BY f.arrival_airport ORDER BY f.flight_id) AS running_total_seats
-- FROM
-- 	flights f
-- JOIN
-- 	(SELECT
-- 		ac.aircraft_code,
-- 		COUNT(s.seat_no) AS seat_count
-- 	FROM
-- 		aircrafts ac
-- 	JOIN
-- 		seats s ON ac.aircraft_code = s.aircraft_code
-- 	GROUP BY
-- 		ac.aircraft_code) sq ON f.aircraft_code = sq.aircraft_code

-- 5.1 Running sum of flights taken by each passenger

SELECT t.passenger_name, ad.city, SUM(1) OVER(PARTITION BY t.passenger_name, ad.city ORDER BY f.scheduled_departure) running_flights
FROM flights f
JOIN airports ad ON f.departure_airport = ad.airport_code
JOIN ticket_flights tf ON f.flight_id = tf.flight_id
JOIN tickets t ON tf.ticket_no = t.ticket_no
LIMIT 50;


-- 5.2 Flight ID for the second most expensive flight for each passenger

-- WITH RankedFlights AS (
-- 	SELECT
-- 		t.passenger_name,
-- 		tf.flight_id,
-- 		tf.amount,
-- 		RANK() OVER(PARTITION BY t.passenger_name ORDER BY tf.amount DESC) as rank
-- 	FROM tickets t
-- 	JOIN ticket_flights tf ON t.ticket_no = tf.ticket_no
-- )
-- SELECT
-- 	passenger_name,
-- 	flight_id,
-- 	amount
-- FROM RankedFlights
-- WHERE rank = 2;

SELECT
	passenger_name,
	flight_id,
	amount
FROM (
	SELECT
		t.passenger_name,
		tf.flight_id,
		tf.amount,
		DENSE_RANK() OVER (PARTITION BY t.passenger_name ORDER BY tf.amount DESC) AS price_rank
	FROM tickets t
	JOIN ticket_flights tf ON t.ticket_no = tf.ticket_no
) AS RankedFlights
WHERE price_rank = 2;
limit(100)
