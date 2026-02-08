import os
import json
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
DATA_FILE = 'data.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/read')
def read():
    data = load_data()
    return render_template('read.html', users=data)

@app.route('/add')
def add_user():
    return render_template('add.html')

@app.route('/adduser', methods=['POST'])
def add_user_post():
    data = load_data()
    new_user = {
        "id": int(request.form['id']),
        "name": request.form['name'],
        "email": request.form['email'],
    }
    data.append(new_user)
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)
    return redirect(url_for('read'))

@app.route('/update/<int:user_id>')
def update(user_id):
    data = load_data()
    user_update = {}
    for user in data:
        if user['id'] == user_id:
            user_update = user
    return render_template('update.html', user=user_update)

@app.route('/updateuser/<int:user_id>', methods=['POST'])
def update_user(user_id):
    data = load_data()
    for user in data:
        if user['id'] == user_id:            
            user['name'] = request.form['name']
            user['email'] = request.form['email']            
            break
    save_data(data)
    return redirect(url_for('read'))

@app.route('/delete/<int:user_id>')
def delete(user_id):
    data = load_data()
    user_delete = {}
    for user in data:
        if user['id'] == user_id:
            user_delete = user
    return render_template('delete.html', user=user_delete)

@app.route('/deleteuser/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    data = load_data()
    data = [user for user in data if user['id'] != user_id]
    save_data(data)
    return redirect(url_for('read'))


@app.route('/Home')
def home():
    return render_template('index.html')

@app.route('/About')
def about():
    return render_template('about.html')

@app.route('/submit', methods = ['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    return render_template('submit.html', name = name, email = email)




if __name__ == '__main__':
    app.run(debug=True)