import pymongo, sys
import os

def get(toFind): #get a person named n

    client = pymongo.MongoClient("mongodb+srv://erinruby:colorado18@yame-project-6ex3z.mongodb.net/test?retryWrites=true") #ERIN's LOGIN
    db = client.prototype #name of the db
    col = client.people #name of the collection
    # toFind = 'erin+ruby'
    print (toFind)
    toFind = toFind.replace(' ', '+')+' '
    # toFind = str(toFind)
    print (type(toFind))
    print (toFind)
    cursor = db.people.find({'name':toFind}) #return everyone in the database
    personarr = []
    for att in cursor:
        print (att)
        n = att['name']
        # n = n.replace('+', ' ')
        print(n)
        personarr.append(n)

    if not personarr:
        print ("We cannot find who you are searching for")
    print (personarr)

# def main():
#
#
# if __name__ == "__main__":
#     main()
