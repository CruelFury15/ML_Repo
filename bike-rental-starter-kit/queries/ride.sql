SELECT DATE(start_time) AS trip_date, COUNT(*) AS rides
FROM ods.trips
GROUP BY trip_date
ORDER BY trip_date;
