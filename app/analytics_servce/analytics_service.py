from flask import Flask, jsonify
import statistics
import mysql.connector
from pymongo import MongoClient

app = Flask(__name__)

MYSQL_HOST = "mysql_db"
MYSQL_USER = "data_user"
MYSQL_PASSWORD = "data_password"
MYSQL_DB = "data_db"

# MongoDB configuration
MONGO_URI = "mongodb://rootadmin:rootpassword@mongo_service:27017/"
MONGO_DB_NAME = "analytics_results"
MONGO_COLLECTION_NAME = "grades_analytics"

mongo_client = MongoClient(MONGO_URI)
db = mongo_client[MONGO_DB_NAME]
collection = db[MONGO_COLLECTION_NAME]

# Connect to the MySQL database
conn = mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DB
)

cursor = conn.cursor()

@app.route('/grades/analytics', methods=['GET'])
def get_grade_analytics():

    # Get the data from mongo
    analytics = collection.find_one({}, {"_id": 0})

    # If no data in MongoDB, compute from MySQL
    if not analytics:

        # Execute a SQL query to fetch the student grades
        cursor.execute("SELECT grade FROM student_grades")
        grades = [row[0] for row in cursor.fetchall()]

        # Do math on the grades
        low_grade = float(min(grades))
        high_grade = float(max(grades))
        avg_grade = float(statistics.mean(grades))

        # Store data in MongoDB
        analytics = {
            "Lowest Grade": low_grade,
            "Highest Grade": high_grade,
            "Average Grade": avg_grade
        }

        collection.insert_one(analytics)

    return jsonify(analytics)

if __name__ == '__main__':
    app.run(debug=True, port=5003)