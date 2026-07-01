
CREATE TABLE groups (
    id INT PRIMARY KEY,
    group_name VARCHAR(50)
);

CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    group_id INT,
    FOREIGN KEY (group_id) REFERENCES groups(id)
);

CREATE TABLE subjects (
    id INT PRIMARY KEY,
    subject_name VARCHAR(50)
);

CREATE TABLE grades (
    id INT PRIMARY KEY,
    student_id INT,
    subject_id INT, 
    grade INT,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (subject_id) REFERENCES subjects(id)
);

INSERT INTO groups VALUES (1, '941-guruh'), (2, '942-guruh');
INSERT INTO students VALUES (1, 'Ali', 1), (2, 'Vali', 1), (3, 'Olim', 2), (4, 'Sardor', NULL);
INSERT INTO subjects VALUES (1, 'Matematika'), (2, 'Fizika'), (3, 'Tarix');
INSERT INTO grades VALUES (1, 1, 1, 95), (2, 2, 1, 85), (3, 3, 2, 92);

