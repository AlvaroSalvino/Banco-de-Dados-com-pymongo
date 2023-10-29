import pprint

import pymongo
import pymongo as pyM

client = pyM.MongoClient("mongodb+srv://AlvaroSalvino:amigoeterno1998@treinobdmongodbatlas.ntcimmt.mongodb.net/?retryWrites=true&w=majority")
db = client.test
posts = db.posts

for post in posts.find():
    pprint.pprint(posts)

print(posts.count_documents({}))
print(posts.count_documents({"author": "Mike"}))
print(posts.count_documents({"tags": "insert"}))

pprint.pprint(posts.find_one({"tags": "insert"}))

print("recuperando info da coleção post de maneira ordenada")
for post in posts.find({}).sort("date"):
    pprint.pprint(post)

result = db.profiles.create_index([('author', pymongo.ASCENDING)], unique=True)

print(sorted(list(db.profiles.index_information())))


user_profile_user = [
    {'user_id': 211, 'name': 'luke'},
    {'user_id': 212, 'name': 'Carlos'}]

result = db.profile_user.insert_many(user_profile_user)

print(f"\nColeções armazenadas no mongoDB")
collections = db.list_collection_names()
for collection in collections:
    print(collection)
