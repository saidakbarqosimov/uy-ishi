SELECT students.name, grades.grade 
FROM students 
LEFT JOIN grades ON students.id = grades.student_id;
