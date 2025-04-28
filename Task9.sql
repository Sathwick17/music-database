
-- 10 queries 

-- 1. INSERT (Add new genre)
INSERT INTO genre (genre_id, name)
VALUES ('G100', 'TestGenre');
select * from genre;

-- 2. INSERT (Add new artist)
INSERT INTO artist (artist_id, name)
VALUES ('ART100', 'TestArtist');
select * from artist;

-- 3. DELETE (Remove one playlist–track mapping)
DELETE FROM playlist_track
WHERE playlist_id = '1'
  AND track_id = '3402';
select * from playlist_track;

-- 4. DELETE (Remove one invoice line)
DELETE FROM invoice_line
WHERE invoice_line_id = '1';
select * from invoice_line;

-- 5. UPDATE Increase price for a specific track
UPDATE track_price
SET unit_price = unit_price * 1.10
WHERE track_id = '1';
select * from track_price;

-- 6. UPDATE Adjust quantity on an invoice line
UPDATE invoice_line
SET quantity = 2
WHERE invoice_line_id = '1';
select * from invoice_line;

-- 7. SELECT with JOIN (Customers and their cities)
SELECT
  c.customer_id,
  c.first_name || ' ' || c.last_name AS customer_name,
  cl.city
FROM customer c
JOIN customer_location cl
  ON c.postal_code = cl.postal_code;

-- 8. SELECT with GROUP BY (Number of tracks per genre)
SELECT
  g.name      AS genre_name,
  COUNT(t.track_id) AS track_count
FROM genre g
JOIN track t
  ON g.genre_id = t.genre_id
GROUP BY g.name;

-- 9. SELECT with ORDER BY (Top 5 longest tracks)
SELECT
  track_id,
  name,
  milliseconds
FROM track
ORDER BY milliseconds DESC
LIMIT 5;

-- 10. SELECT with Subquery (Tracks never sold)
SELECT *
FROM track
WHERE track_id NOT IN (
  SELECT DISTINCT track_id
  FROM invoice_line
);


-- 11. Top Artists by Revenue Generated

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

-- 12. Most Diverse Customers based on Number of Genres Purchased
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

-- Query: Total revenue spent per customer per genre
SELECT 
    c.customer_id,
    g.name AS genre_name,
    SUM(il.quantity * tp.unit_price) AS total_spent
FROM customer c
JOIN invoice i ON c.customer_id = i.customer_id
JOIN invoice_line il ON i.invoice_id = il.invoice_id
JOIN track t ON il.track_id = t.track_id
JOIN track_price tp ON t.track_id = tp.track_id
JOIN genre g ON t.genre_id = g.genre_id
GROUP BY c.customer_id, g.name
ORDER BY total_spent DESC;

CREATE INDEX idx_invoice_customer_id ON invoice(customer_id);
CREATE INDEX idx_invoice_line_invoice_id ON invoice_line(invoice_id);
CREATE INDEX idx_invoice_line_track_id ON invoice_line(track_id);
CREATE INDEX idx_track_genre_id ON track(genre_id);
CREATE INDEX idx_track_price_track_id ON track_price(track_id);
CREATE INDEX idx_track_track_id ON track(track_id);

SELECT 
    c.customer_id,
    g.name AS genre_name,
    SUM(il.quantity * tp.unit_price) AS total_spent
FROM customer c
JOIN invoice i ON c.customer_id = i.customer_id
JOIN invoice_line il ON i.invoice_id = il.invoice_id
JOIN track t ON il.track_id = t.track_id
JOIN track_price tp ON t.track_id = tp.track_id
JOIN genre g ON t.genre_id = g.genre_id
GROUP BY c.customer_id, g.name
ORDER BY total_spent DESC;

