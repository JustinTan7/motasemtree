from flask import Flask, request, jsonify, render_template, redirect, session

app = Flask(__name__)
# This line tells Flask where your static files are located
app.config['STATIC_FOLDER'] = 'static'  
app.secret_key = 'your_secret_key'

users = {
    "SigmaMale": "password",
    "BetaMale": "secret"
}

@app.route('/app/auth', methods=['GET','POST'])
def auth():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            username = request.form['username']
            password = request.form['password']
        else:
            username = request.form['username']
            password = request.form['password']

        # Check if the entered username exists in the dictionary
        if username in users:
            if users[username] == password:
                response = {'message': 'Login successful!'}
                session['username'] = username
                return redirect('/app/home')
            else:
                response = {'message': 'Login failed.'}
                return jsonify(response), 401
        else:
            response = {'message': 'Username not found'}
            return jsonify(response), 404
    
    elif request.method == 'GET':
        return render_template('index.html')

    return "This route is intended for POST requests only.", 400

@app.route('/app/home', methods=['GET', 'POST'])
def home():
    if 'username' in session:  # Check if 'username' is in the session
        return render_template('dashboard.html', username=session['username'])
    else:
        return redirect('/app/home')  # Redirect to login if 'username' is not in the session


if __name__ == '__main__':
    app.run(debug=True, port=5002)