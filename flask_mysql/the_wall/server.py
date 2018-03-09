from flask import Flask, flash, render_template, request, redirect, session
from mysqlconnection import MySQLConnector
import os
import binascii
import md5
import re

app = Flask(__name__)
app.secret_key = "Th!5Is$uPeRSecr37"

mysql = MySQLConnector(app, 'walldb')

def generate_hash(passwd, salt=0):
    if salt == 0:
        salt = binascii.b2a_hex(os.urandom(15))
    else:
        salt = salt

    password = passwd
    hashed_pw = md5.new(password + salt).hexdigest()

    return hashed_pw, salt

def validate_input(firstname, lastname, password,confirmation,email):

    valid_email_regex = re.compile(r'[^@]+@[^@]+\.[^@]+')
    valid_name_regex = re.compile(r'[a-zA-Z]{2,}')
    valid_passwd_regex = re.compile('(?=.*\d)(?=.*[a-z])[a-zA-Z0-9]{8,}')

    if not valid_name_regex.match(firstname) or not valid_name_regex.match(lastname):
        value = 'First and last name must only contain characters or is too short!'
    elif not valid_passwd_regex.match(password):
        value = 'Password must be alphanumeric and at least eight characters long!'
        print "{} = {}".format(password, valid_passwd_regex.match(password))
    elif not password == confirmation:
        value = 'Password and confirmation do not match! Please try again!'
    elif not valid_email_regex.match(email):
        value = 'Invalid email entry!'
    else:
        value = True

    return value

def register_user(user_fname,user_lname,hashed_passwd,salt,user_email):

    db_cols = "INSERT INTO `users` (first_name, last_name, password, salt, email_address, created_at, updated_at)"
    cols_vals = "VALUES (\'{}\',\'{}\',\'{}\',\'{}\',\'{}\', NOW(), NOW())".format(user_fname, user_lname,
                                                                                   hashed_passwd, salt, user_email)
    register_user_query = db_cols + " " + cols_vals
    result = mysql.query_db(register_user_query)

    return result

def post_entry(uid=0,msgid=0,message="",comment=""):

    if uid:
        user_id = uid
    if msgid:
        msg_id = msgid

    if message:
        query = "INSERT INTO `messages` (user_id, message, created_at, updated_at) VALUES (\'{}\',\'{}\', NOW(), NOW())".format(user_id, message)
        entry = message
    elif comment:
        query = "INSERT INTO `comments` (user_id,  message_id, comment, created_at, updated_at) VALUES (\'{}\',\'{}\',\'{}\', NOW(), NOW())".format(user_id, msg_id, comment)
        entry = comment

    result = mysql.query_db(query)

    return result, entry

def get_comments():
    stored_comments_query = 'SELECT messages.id as msg_id, comment as comment_content, comments.created_at ' \
                            'as comment_date, concat_ws(" ", first_name, last_name) as comment_author from comments  ' \
                            'JOIN users on users.id = comments.user_id ' \
                            'JOIN messages on messages.id = comments.message_id order by comment_date ASC;'

    stored_comments = mysql.query_db(stored_comments_query)

    return stored_comments

def get_messages():
    stored_msgs_query = 'SELECT messages.id as msg_id, concat_ws(" ", first_name, last_name) as msg_author, messages.created_at ' \
                        'as msg_date, message as msg_content from users ' \
                        'JOIN messages on messages.user_id = users.id order by msg_date DESC;'
    stored_msgs = mysql.query_db(stored_msgs_query)

    stored_comments = get_comments()
    comments_log = {}
    messages_with_comments = []

    print "comments_log: {}".format(comments_log)

    for comment in stored_comments:
        comment_data = {"comment_author": comment['comment_author'],
                         "comment_content": comment['comment_content'],
                         "comment_date": comment['comment_date'],
                         "message_id": comment['msg_id']}

        if comment['msg_id'] not in comments_log:
            comments_log[comment['msg_id']] = [comment_data]
        else:
            comments_log[comment['msg_id']].append(comment_data)

    # Now check if the message id is present in the list of dictionaries (i.e. the comments_log)
    for message in stored_msgs:
        message_data = dict(msg_author=message['msg_author'], msg_content=message['msg_content'], msg_date=message['msg_date'],
                            msg_id=message['msg_id'], msg_comments=[])

        for i,msgid in enumerate(comments_log):
            if message['msg_id'] == msgid:
                message_data['msg_comments'] = comments_log[msgid]

        messages_with_comments.append(message_data)

    return messages_with_comments

@app.route('/')
def index():
    # Checks for messages if not present initializes the dict key to 0.
    try:
        if session['message'] != "":
            flash(session['message'], "error")
    except:
        session['message'] = ""

    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
@app.route('/login', methods=['GET','POST'])
def login():
    # Sets up the variables with initial values from the form.
    user_email = request.form['email_address']
    password = request.form['user_password']
    session['loggedin'] = False

    # Checks if the user is in the database already.
    query = "SELECT id,first_name, password, salt from users WHERE email_address=\'{}\'".format(user_email)
    user_found = mysql.query_db(query)

    if user_found:
        # Makes sure the password entry is correct.
        encrypted_password, _ = generate_hash(password, salt=user_found[0]['salt'])
        session['first_name'] = user_found[0]['first_name']
        session['uid'] = user_found[0]['id']

        if user_found[0]['password'] == encrypted_password:
            session['loggedin'] = True
            return redirect('/wall')
        else:
            session['message'] = "Oh noes! Invalid password.  Please try again."
    else:
        # Gets ready to register the user.
        flash('User not found! Please register.', "error")

        # Sets up the variables for registration.
        user_fname = request.form['user_name']
        user_lname = request.form['last_name']
        password_conf = request.form['user_password_conf']

        # Validates the input
        form_input_valid = validate_input(user_fname,user_lname,password,password_conf,user_email)

        if form_input_valid == True:

            # Generates hashed password and salt.
            hashed_passwd, salt = generate_hash(password)
            
            # Prepares the data to send to the database.
            result = register_user(user_fname,user_lname,hashed_passwd,salt,user_email)
            if result:
                session['reg_message'] = "Your registration was successful!"
                session['first_name'] = user_fname
                session['uid'] = result
                session['loggedin'] = True
                return redirect('/wall')
            else:
                flash("Registration error! Please contact your administrator")
        else:
            flash(form_input_valid, "error")

    return redirect('/')


@app.route('/wall', methods=['GET', 'POST'])
def wall():
    # We are logged in!
    if 'first_name' in session:
        username = session['first_name']
        flash("Welcome {}".format(username), "msg")

    if 'message' in session:
        flash(session['message'], "success")

    if 'reg_message' in session:
        flash(session['reg_message'], "success")

    # Checks to see if there are messages to display

    messages = get_messages()
    if messages:
        # print "Successfully retrieved {}".format(stored_msgs)
        return render_template('wall.html', data=messages)
    else:
        return render_template('wall.html')


@app.route('/post', methods=['POST'])
def post_message():
    if session['loggedin'] == True:
        uid = session['uid']
        print "uid: {}".format(uid)

        message = request.form['post_message']
        result, entry = post_entry(uid, message=message)
        if result:
            print "{} inserted with id: {}.".format(entry, result)
        else:
            print "Issues adding {} to database: {}".format(message, result)
        return redirect('/wall')
    else:
        return redirect('/')

@app.route('/post/<post_id>/comment', methods=['POST'])
def post_comment(post_id):
    if session['loggedin'] == True:
        uid = session['uid']
        print "uid: {}".format(uid)

        comment = request.form['post_comment']
        result, entry = post_entry(uid, post_id, comment=comment)
        if result:
            print "{} inserted with id: {}.".format(entry, result)
        else:
            print "Issues adding {} to database: {}".format(comment, result)
        return redirect('/wall')
    else:
        return redirect('/')

@app.route('/logout',methods=['POST'])
def logout():
    # Clear all entries.
    session.clear()
    print "session length: {}".format(len(session))

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)