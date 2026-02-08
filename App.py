from flask import Flask, render_template, request

app = Flask(__name__)

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