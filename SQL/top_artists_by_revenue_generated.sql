SELECT 
    a.artist_id,
    a.name AS artist_name,
    ROUND(SUM(tp.unit_price * il.quantity), 2) AS total_revenue
FROM artist a
JOIN album al ON a.artist_id = al.artist_id
JOIN track t ON al.album_id = t.album_id
JOIN track_price tp ON t.track_id = tp.track_id
JOIN invoice_line il ON t.track_id = il.track_id
GROUP BY a.artist_id, a.name
ORDER BY total_revenue DESC
LIMIT 5;