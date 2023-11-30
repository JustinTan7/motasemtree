from flask import Flask, render_template, request, redirect, session, url_for, flash
import requests
from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key = 'your_secret_key'

AUTH_SERVICE_URL = 'http://auth-service:5002/login'
ANALYTICS_URL = 'http://analytics-service:5003/analytics'
SHOW_RESULTS_SERVICE_NAME = 'show-results-service'

app.config['MYSQL_HOST'] = 'mysql'
app.config['MYSQL_USER'] = 'user'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'students_data'


mysql = MySQL(app)

@app.route('/login', methods=['GET', 'POST'])
def login():
    print("Request method is not a POST")

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        data = {'username': username, 'password': password}
        print(f'Data sent to authentication service: {data}')

        response = requests.post(AUTH_SERVICE_URL, json=data)
        print(f'Authentication service response: {response}')

        if response.status_code == 200:
            session['username'] = username
            return redirect('/dashboard')
        else:
            return render_template('login.html', error='Authentication failed. Please try again.')
    else:
        return render_template('login.html', error='')  


@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('input_grades.html')
    else:
        return redirect('/login')
    
@app.route('/input_grades', methods=['GET', 'POST'])
def input_grades():
    if request.method == 'POST':
        student_name = request.form['student_name']
        student_id = request.form['student_id']
        course = request.form['course']
        grade = request.form['grade']

        cursor = mysql.connection.cursor()
        try:
            cursor.execute("INSERT INTO students_grades (student_name, student_id, course, grade) VALUES (%s, %s, %s, %s)",
                           (student_name, student_id, course, grade))
            mysql.connection.commit()
            flash('Data added successfully', 'success')
        except Exception as e:
            flash(f'Error: {str(e)}', 'error')
        finally:
            cursor.close()

        return redirect('/input_grades')

    return render_template('input_grades.html')

def get_show_results_url():
    try:
        # Read the namespace from the mounted service account token file
        with open('/var/run/secrets/kubernetes.io/serviceaccount/namespace', 'r') as namespace_file:
            namespace = namespace_file.read().strip()

        # Use Kubernetes API to get service information
        service_info = requests.get(
            f'http://kubernetes.default.svc/api/v1/namespaces/{namespace}/services/{SHOW_RESULTS_SERVICE_NAME}'
        ).json()

        # Get the external IP address assigned to the service
        external_ip = service_info['status']['loadBalancer']['ingress'][0]['ip']
        
        # Construct the URL
        show_results_url = f'http://{external_ip}:5004/statistics'

        return show_results_url

    except Exception as e:
        print(f'Error getting show-results-service URL: {e}')
        return None

@app.route('/statistics', methods=['GET'])
def statistics():
    show_results_url = get_show_results_url()

    if show_results_url:
        return redirect(show_results_url)
    else:
        return render_template('error.html', error='Error getting show-results-service URL')
    
if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port=5001)

