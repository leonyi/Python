from flask import Flask, flash, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "Th!5IsSecr37"

def randomness():
    rand_num = random.randrange(0,101)

    return rand_num

def set_session():
    rnum = randomness()
    session['rand_num'] = rnum

@app.route('/')
@app.route('/index')
def index():
    set_session()
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    guess_num = int(request.form['guess_num'])
    session_num = session.pop('rand_num')

    if guess_num > session_num:
        flash("Too high!",'error')
    elif guess_num < session_num:
        flash("Too low!", 'error')
    else:
        flash('{} was the number!'.format(guess_num), 'success')

    return redirect('/')

@app.route('/reset', methods=['POST', 'GET'])
def reset():
    set_session()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)