import pymongo
import sys

def main():
    client = pymongo.MongoClient("mongodb+srv://erinruby:colorado18@yame-project-6ex3z.mongodb.net/test?retryWrites=true") #ERIN's LOGIN
    db = client.prototype #name of the db
    col = client.people #name of the collection

    name = sys.argv[1]
    degree = sys.argv[2]
    occupation = sys.argv[3]

    person = {"name": name,
            "degree": degree,
            "occupation": occupation}

    if (db.people.insert_one(person).inserted_id != 0):
        print (name, "successfully added!")
    
if __name__ == '__main__':
    main()
