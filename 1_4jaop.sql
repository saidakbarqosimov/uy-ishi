SELECT students.name, grades.grade 
FROM students 
INNER JOIN grades ON students.id = grades.student_id 
WHERE grades.grade > 90;
