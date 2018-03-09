from flask import Flask, flash, render_template, request, redirect, session
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
app.secret_key = "Th!5IsSecr37"

mysql = MySQLConnector(app, 'emailsdb')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_email', methods=['POST'])
def add_email():
    email_entered = request.form['email_address']
    session['email'] = email_entered
    session['flash_msg'] = ""
    valid_email_regex =re.compile(r'[^@]+@[^@]+\.[^@]+')

    if not email_entered:
        flash("Error: Email cannot be empty!", 'error')
    elif not valid_email_regex.match(email_entered):
        flash("Error: Email ({}) doesn't have a valid format!".format(email_entered), "error")
    else:
        query = "SELECT * from emails where email=\'{}\'".format(email_entered)
        entry_found = mysql.query_db(query)

        if entry_found:
            flash_msg = "Email ({}) is a valid email and it's already in our DB.  Thank you!".format(email_entered)
        else:
            flash_msg = "Email ({}) is a valid email.  Thank you!".format(email_entered)
            query_insert = "INSERT into emails (email, created_at, updated_at) VALUES (':{}', NOW(), NOW())".format(session['email'])
            print query_insert
            mysql.query_db(query_insert)

        # flash(flash_msg, "success")
        session['flash_msg'] = flash_msg

        return redirect('/show_results')

    return redirect('/')

@app.route('/show_results')
def show():
    query = "SELECT * from emails"
    email_list = mysql.query_db(query)

    return render_template('show_results.html', email=session['email'], emails=email_list, flash_msg=session['flash_msg'])

@app.route('/delete_entry', methods=['POST'])
def delete():
    # Add logic to delete.
    query = "DELETE from emails WHERE id=\'{}\'".format(request.form['hidden'])
    print query
    mysql.query_db(query)
    return redirect('/show_results')

if __name__ == "__main__":
    app.run(debug=True)