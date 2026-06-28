SELECT disease, COUNT(*) AS bemorlar_soni 
FROM Bemorlar 
GROUP BY disease 
ORDER BY bemorlar_soni DESC 
LIMIT 1;
