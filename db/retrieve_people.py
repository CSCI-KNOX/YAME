import pymongo
def main():
    client = pymongo.MongoClient("mongodb+srv://erinruby:colorado18@yame-project-6ex3z.mongodb.net/test?retryWrites=true") #ERIN's LOGIN
    db = client.prototype #name of the db
    col = client.people #name of the collection

    cursor = db.people.find({})
    personarr = []

    print (cursor)
    for person in cursor:
        n = person['name']
        personarr.append(n)
    print (personarr)
if __name__ == "__main__":
    main()
