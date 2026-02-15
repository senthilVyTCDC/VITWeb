from flask import Flask, render_template, request, redirect, jsonify
import json
import mysql.connector

app = Flask(__name__)

# MySQL Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root@123",
    database="flaskdb"
)
cursor = db.cursor(dictionary=True)

# Home - Display Records
@app.route('/api/users')
def index():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    print('Hello')
    # return render_template('indexdb.html', users=users)
    return jsonify(users)

# Add Record
# @app.route('/add', methods=['GET', 'POST'])
# def add_user():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
#         db.commit()
#         return redirect('/')
#     return render_template('adddb.html')

@app.route('/api/users', methods=['POST'])
def add_user():
    data = request.get_json()
    cursor.execute(
        "INSERT INTO users (name, email) VALUES (%s, %s)",
        (data['name'], data['email'])
    )
    db.commit()
    return jsonify({"message": "User added"}), 201


# Edit Record
# @app.route('/edit/<int:id>', methods=['GET', 'POST'])
# def edit_user(id):
#     cursor.execute("SELECT * FROM users WHERE id=%s", (id,))
#     user = cursor.fetchone()
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         cursor.execute("UPDATE users SET name=%s, email=%s WHERE id=%s", (name, email, id))
#         db.commit()
#         return redirect('/')
#     return render_template('editdb.html', user=user)

@app.route('/api/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    cursor.execute(
        "UPDATE users SET name=%s, email=%s WHERE id=%s",
        (data['name'], data['email'], id)
    )
    db.commit()
    return jsonify({"message": "User updated"})



# Delete Record
# @app.route('/delete/<int:id>')
# def delete_user(id):
#     cursor.execute("DELETE FROM users WHERE id=%s", (id,))
#     db.commit()
#     return redirect('/')

@app.route('/api/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    cursor.execute("DELETE FROM users WHERE id=%s", (id,))
    db.commit()
    return jsonify({"message": "User deleted"})


if __name__ == '__main__':
    app.run(debug=True)
