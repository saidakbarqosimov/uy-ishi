SELECT author, SUM(pages) AS total_pages 
FROM books 
GROUP BY author;
