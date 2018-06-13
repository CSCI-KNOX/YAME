import pymongo, sys
import os

def getOne(toFind): #get a person named p, if duplicates, finds the most recently added one

    client = pymongo.MongoClient("mongodb+srv://erinruby:colorado18@yame-project-6ex3z.mongodb.net/test?retryWrites=true") #ERIN's LOGIN
    db = client.prototype #name of the db
    col = client.people #name of the collection
    # toFind = toFind.replace(' ', '+')
    cursor = db.people.find({'name':toFind}) #return everyone in the database
    exist = 0
    person = {}
    for att in cursor:
        person = att
        exist = 1
    if not exist:
        print ("Cannot find who you are looking for")
    print (person)
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