
CREATE TABLE books (
    id INT PRIMARY KEY,
    title VARCHAR(100),
    author VARCHAR(100),
    genre VARCHAR(50),
    price DECIMAL(10, 2),
    published_year INT,
    pages INT
);

INSERT INTO books VALUES 
(1, 'O''tkan kunlar', 'Abdulla Qodiriy', 'Roman', 45000.00, 1925, 350),
(2, 'Mehrobdan chayon', 'Abdulla Qodiriy', 'Roman', 42000.00, 1928, 320),
(3, 'Kecha va kunduz', 'Cho''lpon', 'Roman', 40000.00, 1936, 280),
(4, 'Sariq devni minib', 'Xudoyberdi To''xtaboyev', 'Sarguzasht', 35000.00, 1968, 250),
(5, 'Yulduzli tunlar', 'Pirimqul Qodirov', 'Tarixiy', 55000.00, 1978, 520);
