SELECT genre, MAX(price) AS max_price 
FROM books 
GROUP BY genre;
