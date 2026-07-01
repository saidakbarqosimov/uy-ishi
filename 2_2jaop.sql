SELECT genre, COUNT(*) AS book_count 
FROM books 
GROUP BY genre;
