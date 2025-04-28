SELECT
  c.customer_id,
  c.first_name || ' ' || c.last_name AS customer_name,
  cl.city
FROM customer c
JOIN customer_location cl
  ON c.postal_code = cl.postal_code;




