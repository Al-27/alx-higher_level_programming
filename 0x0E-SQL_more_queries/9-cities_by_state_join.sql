-- DESC
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON state_id = states.id ORDER BY cities.id ASC;