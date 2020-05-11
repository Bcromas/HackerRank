SELECT 
CASE
    WHEN Grade<8 THEN 'NULL'
    ELSE Name
END,
Grade, Marks
FROM students
LEFT JOIN grades ON (students.Marks >= grades.Min_Mark AND students.Marks <= grades.Max_Mark) 
ORDER BY Grade DESC, Name;