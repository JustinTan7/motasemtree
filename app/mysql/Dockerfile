FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=password1
ENV MYSQL_DATABASE=students_data
ENV MYSQL_USER=user
ENV MYSQL_PASSWORD=password
ADD init.sql /docker-entrypoint-initdb.d/
EXPOSE 3306