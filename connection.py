from pymongo import MongoClient

# Connect to the MongoDB database
def connect_to_database():
    client = MongoClient("mongodb://localhost:27017")
    return client["basic-crud"]
