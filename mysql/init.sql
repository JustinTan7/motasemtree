CREATE DATABASE IF NOT EXISTS students_data;

USE students_data;

CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(255) NOT NULL,
    student_id VARCHAR(255) NOT NULL,
    course_code VARCHAR(255) NOT NULL,
    grade VARCHAR(2) NOT NULL
);