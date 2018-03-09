from flask import Flask, flash, render_template, request, redirect, session
from mysqlconnection import MySQLConnector

app = Flask(__name__)

mysql = MySQLConnector(app, 'friendsdb')

@app.route('/')
def index():
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)

    return render_template('index.html', all_friends=friends)

@app.route('/create_friend', methods=['POST'])
def create():
    query = "INSERT INTO friends (first_name, last_name, age, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :age, :occupation, NOW(), NOW())"

    # We'll then create a dictionary of data from the POST data received.
    data = {
             'first_name': request.form['first_name'],
             'last_name': request.form['last_name'],
             'age':  request.form['age'],
             'occupation': request.form['occupation']
           }

    print data
    # Run query, with dictionary values injected into the query.
    mysql.query_db(query, data)

    return redirect('/')

## Additional routes to add more functionality.
@app.route('/update_friend/<friend_id>', methods=['POST'])
def update(friend_id):
    query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation WHERE id = :id"
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'last_name': request.form['age'],
             'occupation': request.form['occupation'],
             'id': friend_id
           }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/remove_friend/<friend_id>', methods=['POST'])
def delete(friend_id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': friend_id}
    mysql.query_db(query, data)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)