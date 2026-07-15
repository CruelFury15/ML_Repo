SELECT start_station_name, COUNT(*) AS departures
FROM ods.trips_distance
GROUP BY start_station_name
ORDER BY departures DESC
LIMIT 5;
