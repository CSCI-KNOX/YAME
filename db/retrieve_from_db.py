import pymongo, sys
import os

def getOne(toFind): #get a person named p

    client = pymongo.MongoClient("mongodb+srv://erinruby:colorado18@yame-project-6ex3z.mongodb.net/test?retryWrites=true") #ERIN's LOGIN
    db = client.prototype #name of the db
    col = client.people #name of the collection
    toFind = toFind.replace(' ', '+')

    cursor = db.people.find({'name':toFind}) #return everyone in the database
    exist = 0
    for att in cursor:
        print (att)
        exist = 1
    if not exist:
        print ("Cannot find who you are looking for")
    return cursor

def getAll():

    client = pymongo.MongoClient("mongodb+srv://erinruby:colorado18@yame-project-6ex3z.mongodb.net/test?retryWrites=true") #ERIN's LOGIN
    db = client.prototype #name of the db
    col = client.people #name of the collection

    cursor = db.people.find({})
    personarr = []
    for att in cursor:
        n = att["name"]
        n = n.replace('+', ' ')
        personarr.append(n)
    return personarr

# def main():
#
#
# if __name__ == "__main__":
#     main()
