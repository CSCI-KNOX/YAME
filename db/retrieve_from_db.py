import pymongo, sys
import os, re
import gridfs

def getImage(imageid):
    client = pymongo.MongoClient("mongodb+srv://erinruby:colorado18@yame-project-6ex3z.mongodb.net/test?retryWrites=true") #ERIN's LOGIN
    db = client.prototype #name of the db
    col = client.people #name of the collection

    fs=gridfs.GridFS(db)
    file = fs.find_one({'_id': imageid})
    image = file.read()
    if image:
        return image
    return 0
def searchByLetter(letter):
    client = pymongo.MongoClient("mongodb+srv://erinruby:colorado18@yame-project-6ex3z.mongodb.net/test?retryWrites=true") #ERIN's LOGIN
    db = client.prototype #name of the db
    col = client.people #name of the collection
    cursor = db.people.find({'name': re.compile("^" + letter, re.IGNORECASE)})

    exist = 0
    person = []
    for att in cursor:
        person.append(att)
        exist = 1
    if not exist:
        print ("Cannot find who you are looking for")
        person = 'none'
    return person
def getOne(toFind): #get a person named p, if duplicates, finds the most recently added one
    client = pymongo.MongoClient("mongodb+srv://erinruby:colorado18@yame-project-6ex3z.mongodb.net/test?retryWrites=true") #ERIN's LOGIN
    db = client.prototype #name of the db
    # col = client.people #name of the collection
    cursor = db.people.find({"$or": [{s: re.compile(toFind[s], re.IGNORECASE)} for s in toFind if toFind[s] != '']})

    exist = 0
    person = []
    for att in cursor:
        person.append(att)
        exist = 1
    if not exist:
        print ("Cannot find who you are looking for")
        person = 'none'
    return person

def getOneforDisplay(name): #get a person named name
    client = pymongo.MongoClient("mongodb+srv://erinruby:colorado18@yame-project-6ex3z.mongodb.net/test?retryWrites=true") #ERIN's LOGIN
    db = client.prototype #name of the db
    col = client.people #name of the collection
    cursor = db.people.find({'name': re.compile(name, re.IGNORECASE)})
    exist = 0
    person = []
    for att in cursor:
        person = att
        exist = 1
    if not exist:
        print ("Cannot find who you are looking for")
    return person

def howManyAreSame(toFind): #how many people with the same name??

    client = pymongo.MongoClient("mongodb+srv://erinruby:colorado18@yame-project-6ex3z.mongodb.net/test?retryWrites=true") #ERIN's LOGIN
    db = client.prototype #name of the db
    col = client.people #name of the collection
    toFind = toFind.replace(' ', '+')
    cursor = db.people.find({'name':toFind}) #return everyone in the database
    exist = 0
    count = 0
    person = {}
    for att in cursor:
        count +=1
        exist = 1
    if not exist:
        print ("Cannot find who you are looking for")
    return count

def getAll(): #get all names in the database to print to the screen
    client = pymongo.MongoClient("mongodb+srv://erinruby:colorado18@yame-project-6ex3z.mongodb.net/test?retryWrites=true") #ERIN's LOGIN
    db = client.prototype #name of the db
    col = client.people #name of the collection

    cursor = db.people.find({'hidden' : 0})
    personarr = []
    for att in cursor:
        n = att["name"]
        n = n.replace('+', ' ')
        personarr.append(n)
    return personarr

def getAllContent():
    client = pymongo.MongoClient("mongodb+srv://erinruby:colorado18@yame-project-6ex3z.mongodb.net/test?retryWrites=true") #ERIN's LOGIN
    db = client.prototype #name of the db
    col = client.people #name of the collection

    cursor = db.people.find({'hidden' : 0})
    return cursor
def getPhotoFileName(id):
    client = pymongo.MongoClient("mongodb+srv://erinruby:colorado18@yame-project-6ex3z.mongodb.net/test?retryWrites=true") #ERIN's LOGIN
    db = client.prototype #name of the db
    col = client.people #name of the collection
    fscol = client.fs.files
    cursor = db.fscol.find({'_id':id}) #return everyone in the database
    person = []
    for att in cursor:
        person.append(att)
    print ("HEHHHHHEHEHEHLEOLOLOO", person)
    return person


def getPhoto(dbFileName, tempFileName):
    client = pymongo.MongoClient("mongodb+srv://erinruby:colorado18@yame-project-6ex3z.mongodb.net/test?retryWrites=true") #ERIN's LOGIN
    db = client.prototype #name of the db
    col = client.people #name of the collection
    # fs=gridfs.GridFS(db)
    fs = GridFSBucket(db)
    file = open('/tempImage/{0}'.format(tempFileName), 'wb')
    fs.download_to_stream_by_name(dbFileName, file)


# def main():
#
#
# if __name__ == "__main__":
#     main()
