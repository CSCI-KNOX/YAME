import pymongo
import datetime
import pprint
from pymongo import MongoClient
client = pymongo.MongoClient("mongodb+srv://erinruby:colorado18@yame-project-6ex3z.mongodb.net/test?retryWrites=true")
db = client.prototype
collection = db.people

person = {"name": "Lucile Berkeley Buchanan",
        "degree": "German",
        "occupation": "Teaching",
        "facts": datetime.datetime.utcnow()}
people = db.people
person_id = people.insert_one(person).inserted_id
pprint.pprint(people.find_one())
# print (db.collection_names(include_system_collections=False))
# print (post_id)
