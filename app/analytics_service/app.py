from flask import Flask, jsonify
import statistics
import mysql.connector
from pymongo import MongoClient

app = Flask(__name__)

# MySQL configuration
MYSQL_HOST = "mysql"
MYSQL_USER = "user"
MYSQL_PASSWORD = "password"
MYSQL_DB = "students_data"

# MongoDB configuration
MONGO_URI = "mongodb://rootadmin:rootpassword@app-mongodb-1:27017/"
MONGO_DB_NAME = "analytics_results"
MONGO_COLLECTION_NAME = "grades_analytics"

# Connect to MySQL and MongoDB
conn = mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DB
)

mongo_client = MongoClient(MONGO_URI)
db = mongo_client[MONGO_DB_NAME]
collection = db[MONGO_COLLECTION_NAME]

@app.route('/analytics', methods=['GET'])
def get_grade_analytics():
    try:
        # Get the data from MongoDB
        analytics = collection.find_one({}, {"_id": 0})

        # If no data in MongoDB, compute from MySQL
        if not analytics:
            cursor = conn.cursor()
            cursor.execute("SELECT grade FROM students_grades")
            grades = [row[0] for row in cursor.fetchall()]

            # Do math on the grades
            low_grade = float(min(grades))
            high_grade = float(max(grades))
            avg_grade = float(statistics.mean(grades))

            # Store data in MongoDB
            analytics = {
                "lowest_grade": low_grade,
                "highest_grade": high_grade,
                "average_grade": avg_grade
            }

            collection.insert_one(analytics)

        # Convert the MongoDB document to a regular Python dictionary
        serialized_data = {}
        for key, value in analytics.items():
            serialized_data[key] = value

        return jsonify(serialized_data)

    except Exception as e:
        return str(e), 500  # Handle any exceptions and return an error response



if __name__ == '__main__':
    app.run(debug=True, port=5003, host='0.0.0.0')