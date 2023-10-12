CREATE DATABASE IF NOT EXISTS students_data;

USE students_data;

CREATE TABLE IF NOT EXISTS students_grades (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(255) NOT NULL,
    student_id VARCHAR(255) NOT NULL,
    course_code VARCHAR(255) NOT NULL,
    grade DECIMAL(5,2) NOT NULL
);

INSERT INTO students_grades (student_name, student_id, course_code, grade)
VALUES
    ('Borat Sagdiyev', 'JD001', 'Mathematics', 85.00),
    ('Bilo Sagdiyev', 'JS002', 'Mathematics', 90.00),
    ('Alice Johnson', 'AJ003', 'Biology', 92.00),
    ('Bob Brown', 'BB004', 'Biology', 78.00),
    ('Charlie White', 'CW005', 'Chemistry', 88.00),
    ('Diana Black', 'DB006', 'Physics', 95.00),
    ('Eve Green', 'EG007', 'Physics', 82.00),
    ('Frank Gray', 'FG008', 'English', 89.00),
    ('Grace Blue', 'GB009', 'English', 93.00),
    ('Harry Red', 'HR010', 'History', 81.00);

GRANT SELECT ON students_data.* TO 'user'@'%' WITH GRANT OPTION;

FLUSH PRIVILEGES;

GRANT ALL PRIVILEGES ON *.* TO 'user'@'%' WITH GRANT OPTION;

FLUSH PRIVILEGES;