SELECT author, AVG(price) AS average_price 
FROM books 
GROUP BY author;
