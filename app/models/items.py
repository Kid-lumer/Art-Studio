from .. import mongo
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


class Products:

    def create_item(item):
        return mongo.db.Items.insert_one(item)
    
    def find_items():
        return list(mongo.db.Items.find())
    
    def delete_product():
        return mongo.db.Items.delete_one()
    
 
   
    def delete_item(delete_id):
        return mongo.db.Items.delete_one({"_id": ObjectId(delete_id)})
    
    
    def edit_item(update_id):
        return mongo.db.Items.update_one({"_id": ObjectId(update_id)})