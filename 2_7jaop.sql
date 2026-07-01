SELECT genre, AVG(pages) AS average_pages 
FROM books 
GROUP BY genre;
