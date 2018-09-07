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
def getOne(toFind): #toFind is {}
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

def getAllContent(att=None, value=None):
    client = pymongo.MongoClient("mongodb+srv://erinruby:colorado18@yame-project-6ex3z.mongodb.net/test?retryWrites=true") #ERIN's LOGIN
    db = client.prototype #name of the db
    col = client.people #name of the collection
    if att and value:
        cursor = db.people.find({'hidden' : 0, att :value})
    else:
        cursor = db.people.find({'hidden' : 0})
    return cursor
def getAllCategories(att, value):
    client = pymongo.MongoClient("mongodb+srv://erinruby:colorado18@yame-project-6ex3z.mongodb.net/test?retryWrites=true") #ERIN's LOGIN
    db = client.prototype #name of the db
    col = client.people #name of the collection

    cursor = db.people.find({'iscategory' : 1, att :value})
    return cursor

def getPhotoFileName(id):
    client = pymongo.MongoClient("mongodb+srv://erinruby:colorado18@yame-project-6ex3z.mongodb.net/test?retryWrites=true") #ERIN's LOGIN
    db = client.prototype #name of the db
    col = client.people #name of the collection
    fs=gridfs.GridFS(db)
    cursor = fs.find_one({'_id': id})
    person = []
    exists = 0
    for att in cursor:
        person.append(att)
        exists = 1
    if not exists:
        print ("Cannot find who you are looking for")
    return person


def getPhoto(dbFileName):
    client = pymongo.MongoClient("mongodb+srv://erinruby:colorado18@yame-project-6ex3z.mongodb.net/test?retryWrites=true") #ERIN's LOGIN
    db = client.prototype #name of the db
    col = client.people #name of the collection
    # fs=gridfs.GridFS(db)
    fs=gridfs.GridFSBucket(db)
    if (not os.path.isfile('../form_ui/static/tempImage/{0}'.format(dbFileName))):
        file = open('../form_ui/static/tempImage/{0}'.format(dbFileName), 'wb')
        fs.download_to_stream_by_name(dbFileName, file)


getAllContent("hidden", 0)
# def main():
#
#
# if __name__ == "__main__":
#     main()
