from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

# database connection details
app.config['MYSQL_HOST'] = 'mysql'
app.config['MYSQL_USER'] = 'user'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'students_data'

# Initialize MySQL
mysql = MySQL(app)

# http://localhost:5003/app/input_grades
@app.route('/app/input_grades', methods=['GET', 'POST'])
def input_grades():
    if request.method == 'POST':
        student_name = request.form['student_name']
        student_id = request.form['student_id']
        course_code = request.form['course_code']
        grade = request.form['grade']
        
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO students_data (student_name, student_id, course_code, grade) VALUES (%s, %s, %s, %s)",
                       (student_name, student_id, course_code, grade))
        cursor.execute("select * from students_data")
        data = cursor.fetchall()
        for row in data:
            print(row)
        mysql.connection.commit()
        cursor.close()
        return redirect('/app/input_grades')
    
    return render_template('input_grades.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)