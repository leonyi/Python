from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

@app.route('/dojos', methods=['POST'])
def dojos():
    name = request.form['name']
    address = request.form['address']
    phone = request.form['phone']

    return render_template('dojos.html')

app.run(debug=True)
