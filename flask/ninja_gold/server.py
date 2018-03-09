from flask import Flask, flash, render_template, request, redirect, session
import datetime
import random

app = Flask(__name__)
app.secret_key = "G0ld$ecr3T"

def randomness(start,end):
    num = random.randint(start,end)

    return num

def random_luck():
    earn = random.randint(0,1)

    if earn == 0:
        return False
    else:
        return True

def log_activity(earnings, action, place):
    time_now = datetime.datetime.now()
    log_entry_timestamp = '{:%Y-%m-%d %H:%M:%S}'.format(time_now)
    log_entry = "{} {} golds from the {}! ({})".format(action.title(), earnings, place, log_entry_timestamp)
    print "DEBUG: {}".format(log_entry)
    session['activity'] = action
    session['activity_log'].append(log_entry)


#
@app.route('/')
@app.route('/index')
def index():
    if not 'registered' in session:
        session['gold_count'] = 0
        session['activity_log'] = []
        session['activity'] = ""
        session['registered'] = True

    print "DEBUG: In index! session total: {} and activity log: {}".format(session['gold_count'],session['activity_log'])

    return render_template('index.html', total=session['gold_count'], activity_log=session['activity_log'], activity=session['activity'])

@app.route('/process_money',methods=['POST'])
def process_money():
    form_input = request.form['building']

    for k,v in request.form.items():
        print "DEBUG: {}: {}".format(k,v)

    if form_input == 'farm':
        farm_earnings = randomness(10,20)
        session['gold_count'] += farm_earnings
        log_activity(farm_earnings, "earned", form_input)

    elif form_input == 'cave':
            farm_earnings = randomness(5,10)
            session['gold_count'] += farm_earnings
            log_activity(farm_earnings, "earned", form_input)

    elif form_input == 'house':
            farm_earnings = randomness(2,5)
            session['gold_count'] += farm_earnings
            log_activity(farm_earnings, "earned", form_input)

    elif form_input == 'casino':
            random_outcome = random_luck()
            farm_earnings = randomness(0, 50)

            if random_outcome == True:
                log_activity(farm_earnings, "earned", form_input)
                session['gold_count'] += farm_earnings
            else:
                log_activity(farm_earnings, "lost", form_input)
                session['gold_count'] -= farm_earnings
    else:
        print "ERROR: Couldn't understand that input - {}".format(form_input)

    print "DEBUG: In process_money total is: {}".format(session['gold_count'] )

    return redirect('/')


@app.route('/reset',methods=['POST'])
def reset():
    session['gold_count'] = 0
    session['activity_log'] = []
    session['activity'] = ""

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

