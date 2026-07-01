SELECT * FROM Meva 
WHERE narxi BETWEEN 10000 AND 50000;
SELECT author, COUNT(*) AS book_count 
FROM books 
GROUP BY author;
