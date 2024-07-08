from .. import mongo
from flask_pymongo import PyMongo

class New:
    def create_user(signup_details):
        return mongo.db.signup.insert_one(signup_details)
    
    
    def login(user):
        user = mongo.db.signup.find_one(user)
        return list(mongo.db.signup.find_one({}, {'_id', 0}))
    

    