import pymongo
import datetime
import pprint
from pymongo import MongoClient
client = pymongo.MongoClient("mongodb+srv://erinruby:colorado18@yame-project-6ex3z.mongodb.net/test?retryWrites=true")
client = pymongo.MongoClient("mongodb+srv://courtney:solano@yame-project-6ex3z.mongodb.net/test?retryWrites=true")

db = client.prototype

person = {"name": "Lucile Berkeley Buchanan",
        "degree": "German",
        "occupation": "Teaching",}

# person_id = db.people.insert_one(person).inserted_id
db.people.delete_one(person)
pprint.pprint(people.find_one())
# print (db.collection_names(include_system_collections=False))
# print (post_id)
