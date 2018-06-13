import pymongo, gridfs, random
#for testing capacity of database
def main():
    client = pymongo.MongoClient("mongodb+srv://erinruby:colorado18@yame-project-6ex3z.mongodb.net/test?retryWrites=true") #ERIN's LOGIN
    db = client.prototype #name of the db
    col = client.people #name of the collection
    fruitlist = []
    with open("../../fruits.txt", 'r') as fruits:
        for line in fruits:
            fruitlist.append(line.strip()) #add words from the file into the fruit list

    for i in range(10):
        person = {"name": fruitlist[random.randint(0,len(fruitlist)-1)],
                "degree": fruitlist[random.randint(0,len(fruitlist)-1)],
                "occupation": fruitlist[random.randint(0,len(fruitlist)-1)],
                "photo": fruitlist[random.randint(0,len(fruitlist)-1)],
                "test1":fruitlist[random.randint(0,len(fruitlist)-1)],
                "test2":fruitlist[random.randint(0,len(fruitlist)-1)],
                "test3":fruitlist[random.randint(0,len(fruitlist)-1)],
                "test4":fruitlist[random.randint(0,len(fruitlist)-1)],
                "test5":fruitlist[random.randint(0,len(fruitlist)-1)],
                "test6":fruitlist[random.randint(0,len(fruitlist)-1)],
                "test7":fruitlist[random.randint(0,len(fruitlist)-1)],
                "test8":fruitlist[random.randint(0,len(fruitlist)-1)],
                "test9":fruitlist[random.randint(0,len(fruitlist)-1)],
                "test10":fruitlist[random.randint(0,len(fruitlist)-1)],
                "test11":fruitlist[random.randint(0,len(fruitlist)-1)],
                "test12":fruitlist[random.randint(0,len(fruitlist)-1)],
                "test13":fruitlist[random.randint(0,len(fruitlist)-1)],
                "test14":fruitlist[random.randint(0,len(fruitlist)-1)],
                "test15":fruitlist[random.randint(0,len(fruitlist)-1)],
                "test16":fruitlist[random.randint(0,len(fruitlist)-1)],
                "test17":fruitlist[random.randint(0,len(fruitlist)-1)],
                "test18":fruitlist[random.randint(0,len(fruitlist)-1)]
                }
        id = db.people.insert_one(person).inserted_id

if __name__ == '__main__':
    main()
