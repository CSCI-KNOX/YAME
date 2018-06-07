import pymongo
import sys
import gridfs
import os
#hello
#example: python add_person.py erin cs student
def main():
    client = pymongo.MongoClient("mongodb+srv://erinruby:colorado18@yame-project-6ex3z.mongodb.net/test?retryWrites=true") #ERIN's LOGIN
    db = client.prototype #name of the db
    col = client.people #name of the collection

    name = sys.argv[1]
    degree = sys.argv[2]
    occupation = sys.argv[3]
    photo = sys.argv[4]

    fs=gridfs.GridFS(db)
    im = fs.put(open('../form_ui/uploads/{0}'.format(photo), 'rb'), filename='{0}'.format(photo)) #store the photo in the db


    person = {"name": name,
            "degree": degree,
            "occupation": occupation,
            "photo": im}

    if (db.people.insert_one(person).inserted_id != 0):
        print (name, "successfully added!")

    pup = db.fs.files.find({'_id':im}) #find the photo for the person that just got inserted
    for att in pup:
        p = att['filename']

    os.system("open ../form_ui/uploads/{0}".format(photo)) #check to see if the photo uploads correctly

if __name__ == '__main__':
    main()
