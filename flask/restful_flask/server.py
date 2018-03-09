from flask import Flask, flash, render_template, request, redirect, session
from flask_restful import Resource, Api 
from mysqlconnection import MySQLConnector
import os
import binascii
import md5
import re

PORT = 5000

app = Flask(__name__)
api = Api(app)

app.secret_key = "Th!5Is$uPeRSecr37"

items = []

def abort_if_item_doesnt_exist(item_id):
    if item_id not in items:
        abort(404, message="Item {} doesn't exist".format(item_id)) 

# ---- API Resources ---- #
class Item(Resource):
    def get(self, name):
        # next will give us the next item matched by the filter function.
        item = next(filter(lambda item: item['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

        #for item in items:
        #    if item['name'] == name:
        #        return item
        #else:
        #    return({'error': 'Item not found!'}, 404)

    
    def post(self, name):
        if next(filter(lambda item: item['name'] == name, items), None) is not None:
            return {'message': 'An item with that name already exists {}!'.format(name)}, 400            
        else:
            data = request.get_json()
            try:
                item = { 'name': name, 'price': data['price']}
                items.append(item)
                return(item, 201)
            except Exception as err:
                return({'error': "{}".format(err)})

class Items(Resource):
    def get(self):
       if items:
            return({'items': items})
       else:
            return({'error': 'No items available'})

# GET http://localhost:5000/item/item_name
api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')

if __name__ == "__main__":
    app.run(debug=True, port=PORT)
