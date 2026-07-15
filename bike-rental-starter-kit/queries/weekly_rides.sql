-- This query analyzes ride volume by day of the week.
-- EXTRACT(DOW FROM trip_start_time) returns the numeric day of week (0=Sunday, 1=Monday, ..., 6=Saturday).
-- COUNT(*) counts total rides starting on each day.
-- GROUP BY day_of_week groups trips by weekday number.
-- ORDER BY rides DESC sorts results so the busiest day appears first.
SELECT EXTRACT(DOW FROM start_time) AS day_of_week, COUNT(*) AS rides
FROM ods.trips
GROUP BY day_of_week
ORDER BY rides DESC;
