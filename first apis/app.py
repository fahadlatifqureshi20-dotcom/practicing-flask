#from dotenv import load_dotenv
#load_dotenv() : to force to read .env file 

from flask import Flask , request 
import uuid
from db import items
app = Flask (__name__)

#http://127.0.0.1:5000 / get-items

@app.get('/items')

def get_items():
# return {"items": list(items.values()) } : to hide unique id
    return {"items":items }

#fetching single item
@app.get('/item')
def get_item():
    id = request.args.get('id')   # get the id from URL query
    try:
        return items[id]
    except KeyError:
        return {"message": "item not found"}, 404



#http://127.0.0.1:5000/additem
#adding item

@app.post('/item')

def add_item():
   request_data= request.get_json()
   if 'name' not in request_data or 'price' not in request_data:
       return{'message':'input is incomplete '},400
   items[uuid.uuid4().hex] = request_data
   return { "message": "msg added succcessfully"}, 201

#updatind the item

@app.put('/item')

def update_item():
      id= request.args.get('id')
      if id==None:
          return{'message':'id not found'},404

    # Validate ID, as an invalid one would create a new item instead of updating.
      if id in items.keys():
        request_data = request.get_json()
        if 'name' not in request_data or 'price' not in request_data: 
            return{'message':'input in not complete'},404
        items[id]=request.get_json()
        return {'message': 'item add successfully'}, 200
      else: 
          return{'message':'key not found'},404
      

#deleating data , args= arguments 
@app.delete('/item')

def del_item():
    id = request.args.get('id')
    if id==None:
        return{'message':'id not found'},404
    if id in items.keys():
        del items[id]
        return {"message":"data deleted"} , 200
    return{'message':'record not found'} , 404

for rule in app.url_map.iter_rules():
    print(rule)
