from flask import Flask, request, jsonify, render_template, redirect, session

app = Flask(__name__)
# This line tells Flask where your static files are located
app.config['STATIC_FOLDER'] = 'static'  
app.secret_key = 'your_secret_key'

users = {
    "Borat": "password",
    "Bilo": "secret"
}


@app.route('/login', methods=['POST'])
def auth():
    if request.is_json:
        data = request.json  # Access JSON data
        username = data.get('username')
        password = data.get('password')

        if username in users:
            if users[username] == password:
                response = {'message': 'Login successful!'}
                session['username'] = username
                return jsonify(response), 200
            else:
                response = {'message': 'Login failed.'}
                return jsonify(response), 401
        else:
            response = {'message': 'Username not found'}
            return jsonify(response), 404

    return "This route is intended for POST requests only.", 400


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)