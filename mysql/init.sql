CREATE DATABASE IF NOT EXISTS students_data;

USE students_data;

CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(255),
    student_id INT,
    course_code VARCHAR(255),
    grade VARCHAR(2)
);