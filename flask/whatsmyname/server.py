from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    visitor = request.form['name']
    print "Processed: ", visitor
    return redirect('/')

app.run(debug=True)