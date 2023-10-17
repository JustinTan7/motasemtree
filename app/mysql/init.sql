CREATE DATABASE IF NOT EXISTS students_data;

USE students_data;

CREATE TABLE IF NOT EXISTS students_grades (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(255) NOT NULL,
    student_id VARCHAR(255) NOT NULL,
    course VARCHAR(255) NOT NULL,
    grade DECIMAL(5,2) NOT NULL
);

INSERT INTO students_grades (student_name, student_id, course, grade)
VALUES
    ('Borat Sagdiyev', 'JD001', 'Mathematics', 85.00),
    ('Bilo Sagdiyev', 'JS002', 'Mathematics', 90.00),
    ('Toji Fushiguro', 'AJ003', 'Advanced Heavenly Restriction II', 100),
    ('Gojo Satoru', 'BB004', 'Adavnced Reversed Cursed Techniques', 100),
    ('Lebron James', 'CW005', 'GOAT Behaviour', 95.00),
    ('Chris Paul', 'DB006', 'Intro To Never Winning a Ring', 95.00),
    ('Draymond Green', 'EG007', 'How To Get Flagrants 101', 82.00),
    ('Makima', 'FG008', 'Expert Manipulation 400', 94.00),
    ('Tanjiro Kamado', 'GB009', 'How To Power Scale Quickly ', 93.00),
    ('Charles Barkley', 'HR010', 'Banging in the Paint 101', 81.00);

GRANT SELECT ON students_data.* TO 'user'@'%' WITH GRANT OPTION;

FLUSH PRIVILEGES;

GRANT ALL PRIVILEGES ON *.* TO 'user'@'%' WITH GRANT OPTION;

FLUSH PRIVILEGES;