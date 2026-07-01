SELECT published_year, COUNT(*) AS book_count 
FROM books 
GROUP BY published_year;
