from flask import Flask, flash, render_template, request, redirect, session
from mysqlconnection import MySQLConnector
import os
import binascii
import md5
import re

app = Flask(__name__)
app.secret_key = "Th!5Is$uPeRSecr37"

mysql = MySQLConnector(app, 'loginsdb')

def generate_hash(passwd, salt=0):
    if salt == 0:
        salt = binascii.b2a_hex(os.urandom(15))
    else:
        salt = salt

    password = passwd
    hashed_pw = md5.new(password + salt).hexdigest()

    return hashed_pw, salt


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
@app.route('/login', methods=['GET','POST'])
def login():
    # Sets up the variables with initial values from the form.
    user_email = request.form['email_address']
    password = request.form['user_password']

    # Compiles the regular expressions to do input validation.
    valid_email_regex = re.compile(r'[^@]+@[^@]+\.[^@]+')
    valid_name_regex = re.compile(r'[a-zA-Z]+')
    valid_passwd_regex = re.compile('(?=.*\d)(?=.*[a-z])[a-zA-Z0-9]{8,}')

    # Checks if the user is in the database already.
    query = "SELECT first_name, password, salt from users WHERE email_address=\'{}\'".format(user_email)
    user_found = mysql.query_db(query)

    if user_found:
        # Makes sure the password entry is correct.
        encrypted_password, _ = generate_hash(password, salt=user_found[0]['salt'])
        session['first_name'] = user_found[0]['first_name']

        print "session contents: {}".format(session)

        print "encrypted password: {}".format(encrypted_password)

        if user_found[0]['password'] == encrypted_password:
            return redirect('/home')
        else:
            flash("Oh noes! Invalid password.  Please try again.")

    else:
        user_fname = request.form['user_name']
        user_lname = request.form['last_name']
        password_conf = request.form['user_password_conf']

        if not valid_name_regex.match(user_fname) or not valid_name_regex.match(user_lname):
            flash("First and last name must only contain characters!", "error")
        elif (len(user_fname) <= 2 or len(user_lname) <= 2):
            flash("First name or last name too short!", "error")
        elif not valid_passwd_regex.match(password):
            flash("Password must be alphanumeric and at least eight character long", "error")
        elif not password == password_conf:
            flash("Password and confirmation don't match! Please try again!", "error")
        elif not valid_email_regex.match(user_email):
            flash("Invalid email entry!", "error")
        else:
            # Generates hashed password and salt.
            hashed_passwd, salt = generate_hash(password)
            
            # Prepares the data to send to the database.
            db_cols = "INSERT INTO `users` (first_name, last_name, password, salt, email_address, created_at, updated_at)"
            cols_vals = "VALUES (\'{}\',\'{}\',\'{}\',\'{}\',\'{}\', NOW(), NOW())".format(user_fname,user_lname,hashed_passwd,salt,user_email)
            
            # Registers the user.
            register_user_query = db_cols + " " + cols_vals
            result = mysql.query_db(register_user_query)
            
            if result:
                flash("Registration success!", "success")
            else:
                flash("Registration error! Please contact your administrator", "error")

    return redirect('/')


@app.route('/home')
def home():
    if 'first_name' in session:
        username = session['first_name']
        flash("Welcome {}".format(username), "msg")

    return render_template('home.html')

@app.route('/logout',methods=['POST'])
def logout():
    # Remove the user_name from the session if it's present.
    popped= session.pop('first_name', None)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)