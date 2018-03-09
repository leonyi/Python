from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'ThisisSuperSecret'
counter = 0

@app.route('/')
@app.route('/index')
def index():
    try:
        session['counter'] += 1
    except KeyError:
        session['counter'] = 0

    return render_template('index.html')

@app.route('/add_two', methods=['POST'])
def add_two():
    session['counter'] += 1

    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['counter'] = 0

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)