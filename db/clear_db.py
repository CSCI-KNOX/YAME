import pymongo, gridfs
def main():
    client = pymongo.MongoClient("mongodb+srv://erinruby:colorado18@yame-project-6ex3z.mongodb.net/test?retryWrites=true") #ERIN's LOGIN
    db = client.prototype #name of the db
    col = client.people #name of the collection
    db.people.delete_many({})

    fs=gridfs.GridFS(db)
    db.fs.files.delete_many({})
    db.fs.chunks.delete_many({})

if __name__ == '__main__':
    main()
