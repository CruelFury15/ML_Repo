-- Top 10 most popular routes
SELECT 
    start_station_name,
    end_station_name AS destination,
    COUNT(*) AS trip_count
FROM ods.trips_distance
GROUP BY start_station_name, end_station_name
ORDER BY trip_count DESC
LIMIT 10;