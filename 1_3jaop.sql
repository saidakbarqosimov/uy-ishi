SELECT subjects.subject_name, grades.grade 
FROM grades 
RIGHT JOIN subjects ON grades.subject_id = subjects.id;
