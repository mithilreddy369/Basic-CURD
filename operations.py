# Find documents that match a specific condition
def find_documents(db, query):
    collection = db["mycollection"]
    documents = collection.find(query)
    for document in documents:
        print(document)

# Insert a document into the collection
def insert_document(db, document):
    collection = db["mycollection"]
    collection.insert_one(document)
    print("Document inserted successfully.")

# Update documents that match a specific condition
def update_documents(db, query, new_values):
    collection = db["mycollection"]
    collection.update_many(query, new_values)
    print("Documents updated successfully.")

# Delete documents that match a specific condition
def delete_documents(db, query):
    collection = db["mycollection"]
    collection.delete_many(query)
    print("Documents deleted successfully.")
