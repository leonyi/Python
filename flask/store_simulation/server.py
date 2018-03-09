from flask import Flask, flash, render_template, request, redirect, session, jsonify
from mysqlconnection import MySQLConnector
import os
import binascii
import md5
import re

# Set the port flask will listen on #
PORT = 5000

app = Flask(__name__)
app.secret_key = "Th!5Is$uPeRSecr37"

mysql = MySQLConnector(app, 'storedb')

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
               'name': 'My Item',
               'price': 15.99  
            }
        ]
    }
]

@app.route('/')
def index():
     return render_template('index.html') 

# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json() 
    new_store = {
        'name': request_data['name'],
        'items': []
    }   
    stores.append(new_store)
    return jsonify(new_store)

# Accessed at GET http://localhost:5000/store
@app.route('/store/')
def retrieve_stores():
    return jsonify({'stores': stores})

# GET /store/<string:name>
# Accessed at GET http://localhost:5000/store/store_name
@app.route('/store/<string:name>', methods=['GET'])
def retrieve_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
        else:
            return jsonify({'error': 'Store not found!'})

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()

    for store in stores:
        if store['name'] == name:
            new_item = {
                'name':  request_data['name'],
                'price': request_data['price']
            }  
            store['items'].append(new_item) 
            return jsonify(store)

    return jsonify({'error': 'Requested store not found!'})


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['GET'])
def retrieve_items_in_store(name):
    for store in stores:
        if store['name'] == name:
                return jsonify(store['items'])
        else:
             return jsonify({'error': 'No store by that name found!'})       

if __name__ == "__main__":
    app.run(debug=True, port=PORT)
