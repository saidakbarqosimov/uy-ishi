SELECT students.name, groups.group_name 
FROM students 
INNER JOIN groups ON students.group_id = groups.id;
