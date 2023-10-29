import datetime
import pprint

import pymongo as pyM

client = pyM.MongoClient("mongodb+srv://AlvaroSalvino:amigoeterno1998@treinobdmongodbatlas.ntcimmt.mongodb.net/?retryWrites=true&w=majority")

db = client.test
collection = db.test_collection
print(db.test_collection)

# Definição de insfor para compor o doc
post = {
    "author": "Mike",
    "text": "My first mongodb application based on pyhon",
    "tags": ["mongodb", "python3", "pymongo"],
    "date": datetime.datetime.utcnow()
}

# preparando para submeter as infos
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)

pprint.pprint(db.posts.find_one())

#bulk inserts
new_posts = [{
    "author": "Mike",
    "text": "Another post",
    "tags": ["bulk", "post", "insert"],
    "date": datetime.datetime.utcnow()
    },
    {
        "author": "Alvaro Salvino",
        "text": "Alguma coisa teste",
        "title": "Aprendendo Mongo",
        "date": datetime.datetime(2022, 4, 7, 12, 40)}]

result = posts.insert_many(new_posts)
print(result.inserted_ids)

print(f"\nRecuperação final")
pprint.pprint(db.posts.find_one({"author": "Alvaro Salvino"}))

print(f"\nDocumentos presentes na coleção posts")
for post in posts.find():
    pprint.pprint(post)
