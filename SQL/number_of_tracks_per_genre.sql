SELECT
  g.name      AS genre_name,
  COUNT(t.track_id) AS track_count
FROM genre g
JOIN track t
  ON g.genre_id = t.genre_id
GROUP BY g.name;