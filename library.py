from pymongo import MongoClient

connection_string = "mongodb://localhost:27017"

# Create a MongoClient object
client = MongoClient(connection_string)

# Access a database (create it if it doesn't exist)
db = client['e-commerce']

# Access a collection (similar to a table in relational databases)
collection = db['orders']

# Example: Insert a document into the collection
# sample_data = [
#     {"customerID": 1, "productsPurchased": [{"product": "Laptop", "quantity": 1, "price": 75000}, {"product": "Coffee Maker", "quantity": 1, "price": 4500}], "totalAmount": 79500, "status": "shipped"},
#     {"customerID": 2, "productsPurchased": [{"product": "Wireless Headphones", "quantity": 2, "price": 12000}, {"product": "Blender", "quantity": 1, "price": 3000}], "totalAmount": 27000, "status": "pending"},
#     {"customerID": 3, "productsPurchased": [{"product": "Smartphone", "quantity": 1, "price": 60000}], "totalAmount": 60000, "status": "shipped"},
#     {"customerID": 4, "productsPurchased": [{"product": "Blender", "quantity": 1, "price": 3000}, {"product": "Laptop", "quantity": 1, "price": 75000}], "totalAmount": 78000, "status": "pending"}

# ]



# collection.insert_many(sample_data)

result = collection.update_many(
    {},  # This empty filter matches all documents in the collection
    {"$set": {"newID": bson.ObjectId()}}  # Assign a new ObjectId to 'newID'
)

# Retrieve documents from the collection
# { "publication": { "$gt": 2000 } }
results = collection.find() 
for document in results:     
    print(document)

# Close the connection when done
client.close()
