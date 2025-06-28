from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)


db = mysql.connector.connect(
    host="localhost",       
    user="root",
    password="root",
    database="sagar"
)
cursor = db.cursor(dictionary=True)

@app.route('/add_record', methods=['POST'])
def add_record():
    data = request.json
    user_name = data.get('user_name')
    exercise = data.get('exercise')
    weight = data.get('weight')
    reps = data.get('reps')
    record_date = data.get('record_date')

    cursor.execute(
        "INSERT INTO records (user_name, exercise, weight, reps, record_date) VALUES (%s, %s, %s, %s, %s)",
        (user_name, exercise, weight, reps, record_date)
    )
    db.commit()
    return jsonify({"message": "Record added successfully"}), 201

@app.route('/get_records', methods=['GET'])
def get_records():
    cursor.execute("SELECT * FROM records")
    records = cursor.fetchall()
    return jsonify(records)

@app.route('/get_records/<username>', methods=['GET'])
def get_records_by_user(username):
    cursor.execute("SELECT * FROM records WHERE user_name = %s", (username,))
    records = cursor.fetchall()
    return jsonify(records)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
