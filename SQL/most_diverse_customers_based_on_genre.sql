SELECT 
    c.customer_id,
    c.first_name || ' ' || c.last_name AS customer_name,
    COUNT(DISTINCT t.genre_id) AS genres_purchased
FROM customer c
JOIN invoice i ON c.customer_id = i.customer_id
JOIN invoice_line il ON i.invoice_id = il.invoice_id
JOIN track t ON il.track_id = t.track_id
GROUP BY c.customer_id, customer_name
ORDER BY genres_purchased DESC
LIMIT 5;