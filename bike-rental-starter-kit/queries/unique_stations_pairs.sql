SELECT DISTINCT 
    start_station_name,
    start_station_id,
    end_station_name AS destination,
    end_station_id AS destination_id
FROM ods.trips_distance
ORDER BY destination ASC;
