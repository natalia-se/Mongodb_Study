from pymongo import MongoClient

connection_string = "mongodb://localhost:27017"

# Create a MongoClient object
client = MongoClient(connection_string)

# Access a database (create it if it doesn't exist)
db = client['restaurants']

# Access a collection (similar to a table in relational databases)
collection = db['restaurants']

# Example: Insert a document into the collection
# sample_data = [{
#   "address": {
#      "building": "1007",
#      "coord": [ -73.856077, 40.848447 ],
#      "street": "Morris Park Ave",
#      "zipcode": "10462"
#   },
#   "borough": "Bronx",
#   "cuisine": "Bakery",
#   "grades": [
#      { "date": { "$date": 1393804800000 }, "grade": "A", "score": 2 },
#      { "date": { "$date": 1378857600000 }, "grade": "A", "score": 6 },
#      { "date": { "$date": 1358985600000 }, "grade": "A", "score": 10 },
#      { "date": { "$date": 1322006400000 }, "grade": "A", "score": 9 },
#      { "date": { "$date": 1299715200000 }, "grade": "B", "score": 14 }
#   ],
#   "name": "Morris Park Bake Shop",
#   "restaurant_id": "30075445"
# }]



# collection.insert_many(sample_data)

# Retrieve documents from the collection
# results = collection.find() 
# for document in results:     
#     print(document)

# Write a MongoDB query to display the fields restaurant_id, name, borough and cuisine for all the documents
#results = collection.find({}, {"name": 1, "borough": 1, "cuisine": 1,  "_id": 0})
# for document in results:
#     print(document)

#Write a MongoDB query to display the fields restaurant_id, name, borough and zip code, but exclude the field _id for all the documents in the collection restaurant.
# results = collection.find({}, {"restaurant_id": 1, "name": 1, "borough": 1, "address.zipcode": 1,  "_id": 0})
# for document in results:
#     print(document)

# 5. Write a MongoDB query to display all the restaurant which is in the borough Bronx.
# results = collection.find({"borough": "Bronx"}).limit(5)
# for document in results:
#     print(document)

#7.Write a MongoDB query to display the next 5 restaurants after skipping first 5 which are in the borough Bronx.
# results = collection.find({"borough": "Bronx"}).skip(5).limit(5)
# for document in results:
#     print(document)

#8. Write a MongoDB query to find the restaurants who achieved a score more than 90.
# results = collection.find({"grades": {
#         "$elemMatch": { "score": { "$gt": 90 } }
#     }}, {"name": 1, "grades": 1, "_id": 0})
# for document in results:
#     print(document)

#9. Write a MongoDB query to find the restaurants that achieved a score, more than 80 but less than 100.
# results = collection.find({"grades": {
#         "$elemMatch": { "score": { "$gt": 80,"$lt": 100 } }
#     }}, {"name": 1, "grades": 1, "_id": 0})
# for document in results:
#     print(document)

#10. Write a MongoDB query to find the restaurants which locate in latitude value less than -95.754168.
results = collection.find({"address.coord": { "$lt": -95.754168 } }, {"name": 1, "address": 1, "_id": 0})
for document in results:
    print(document)

    
# Close the connection when done
client.close()
