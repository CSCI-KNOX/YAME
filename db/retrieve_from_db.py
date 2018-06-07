import pymongo, sys
import os
def main():
    client = pymongo.MongoClient("mongodb+srv://erinruby:colorado18@yame-project-6ex3z.mongodb.net/test?retryWrites=true") #ERIN's LOGIN
    db = client.prototype #name of the db
    col = client.people #name of the collection

    # cursor = db.people.find({}) #find everything in the db
    # personarr = []
    #
    # print (cursor)
    # for person in cursor:
    #     n = person['name'] #only take save the names of the people
    #     personarr.append(n)
    # print (personarr)

#i want to find all the computer science people
    att = sys.argv[1] #what att you want to query
    val = sys.argv[2] #what value of the att you are looking for
    cursor = db.people.find({att:val})
    personarr = []
    for person in cursor:
        n = person['name']
        personarr.append(n)
    if not personarr:
        print ("We cannot find who you are searching for")
    print (personarr)
if __name__ == "__main__":
    main()
