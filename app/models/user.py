from .. import mongo
from flask_pymongo import PyMongo

class New:
   
    def create_user(signup_details):
        known_user = New.find_user_by_email(signup_details['email'])
        if known_user:
            return False  # User already exists
        else:
            # Insert the new user into the database
            mongo.db.signup.insert_one(signup_details)
            return True  # User created successfully
    
    
    def find_user_by_email(email):
        return mongo.db.signup.find_one({'email': email})

    def find_user_by_email_and_password(email, password):
        return mongo.db.signup.find_one({'email': email, 'password': password})

    
    
    
   

    