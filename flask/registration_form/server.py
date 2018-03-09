from flask import Flask, flash, request, redirect, session

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route("")

