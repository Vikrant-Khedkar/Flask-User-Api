from flask import Flask, request, jsonify
from flask_restful import Resource, Api ,reqparse
from pymongo import MongoClient
import hashlib


app = Flask(__name__)
api = Api(app)

MONGO_HOST = 'my-mongo-container'
MONGO_PORT = 27017
MONGO_DB = 'user_db'
MONGO_COLLECTION = 'users'

client = MongoClient(MONGO_HOST, MONGO_PORT)
db = client[MONGO_DB]
collection = db[MONGO_COLLECTION]





class UserResource(Resource):
    def post(self):
        data = request.get_json()
        if data and 'name' in data and 'email' in data and 'password' in data:
            password = hashlib.sha256(data['password'].encode()).hexdigest()

            user = {
                'userid': data['id'],
                'name': data['name'],
                'email': data['email'],
                'password': password
            }
            result = collection.insert_one(user)
            if result.inserted_id:
                return {'message': 'User created successfully'}, 201
            else:
                return {'message': 'Failed to create user'}, 500
        else:
            return {'message': 'Invalid data'}, 400
    
    def put(self,userid):
        data = request.get_json()
        if data and 'name' in data and 'email' in data and 'password' in data:
            password = hashlib.sha256(data['password'].encode()).hexdigest()

            user = {
                'userid': data['id'],
                'name': data['name'],
                'email': data['email'],
                'password': password
            }
            result = collection.find_one_and_update({'userid':userid},{'$set':user})
           
        else:
            return {'message': 'Invalid data'}, 400
    
    
    def get(self):
            users = list(collection.find({},{'_id':0}))
            return jsonify(users)

    
    def delete(self,userid):
        user = collection.find_one_and_delete({'userid':userid},{'_id':0})
        if user:
            return {"message":"{0}deleted".format(user)}

class GetUserbyId(Resource):
    def get(self,userid):
        user = collection.find_one({'userid': userid}, {'_id': 0})
        if user:
            return user, 200
        else:
            return {"message": "User not found"}, 404


api.add_resource(UserResource, '/users')
api.add_resource(GetUserbyId,'/users/<string:userid>')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
