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

    for i in range(15):
        person = {"name": fruitlist[random.randint(0,len(fruitlist)-1)],
                "degree": fruitlist[random.randint(0,len(fruitlist)-1)],
                "school": fruitlist[random.randint(0,len(fruitlist)-1)],
                "year": fruitlist[random.randint(0,len(fruitlist)-1)],
                "occupation": fruitlist[random.randint(0,len(fruitlist)-1)],
                "facts": fruitlist[random.randint(0,len(fruitlist)-1)],
                "image": fruitlist[random.randint(0,len(fruitlist)-1)],
                "hidden": random.randint(0,1),
                }
        id = db.people.insert_one(person).inserted_id

if __name__ == '__main__':
    main()
