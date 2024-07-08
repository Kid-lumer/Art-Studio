from .. import mongo
from flask_pymongo import PyMongo


class Products:

    def create_item(item):
        return mongo.db.Items.insert_one(item)
    
   
