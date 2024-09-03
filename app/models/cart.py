from .. import mongo
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

class Cart:
   def cart_item(item):
        return mongo.db.Items.insert_one(item)