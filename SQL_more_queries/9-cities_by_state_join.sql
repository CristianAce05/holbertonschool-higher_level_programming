-- Lists all cities in the database hbtn_0d_usa
-- Each record displays: cities.id - cities.name - states.name
-- Sorted in ascending order by cities.id
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
