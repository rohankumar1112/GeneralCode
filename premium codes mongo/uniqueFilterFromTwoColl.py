from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient('mongodb://localhost:27017/')

# Select the database and collections
db = client['demo3']
collection1 = db['cyber_data_new']
print(collection1.count_documents({}))
collection2 = db['ForumData_filtered']
print(collection2.count_documents({}))
unique_collection = db['allData']


common_set = set([doc['url'] for doc in collection1.find()])

# # Iterate over the documents in collection1 and insert those that are not in collection2 into unique_collection
# for doc in collection1.find():
#     if doc['_id'] not in common_set:
#         unique_collection.insert_one(doc)

# Iterate over the documents in collection2 and insert those that are not in collection1 into unique_collection
for doc in collection2.find():
    if doc['url'] not in common_set:
        unique_collection.insert_one(doc)

print(unique_collection.count_documents())