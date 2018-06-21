import pymongo
import sys
import gridfs
import os
#hello
#example: python add_person.py erin cs student
def addOne(name, degree, school, ex, year, occupation, facts, photo, hidden):
    client = pymongo.MongoClient("mongodb+srv://erinruby:colorado18@yame-project-6ex3z.mongodb.net/test?retryWrites=true") #ERIN's LOGIN
    db = client.prototype #name of the db
    col = client.people #name of the collection

    # name = sys.argv[1]
    # degree = sys.argv[2]
    # occupation = sys.argv[3]
    # photo = sys.argv[4]

    fs=gridfs.GridFS(db)
    im = fs.put(open('../form_ui/static/imj/{0}'.format(photo), 'rb'), filename='{0}'.format(photo)) #store the photo in the db
    person = {"name": name,
            "degree": degree,
            "school": school,
            "ex": ex,
            "year": year,
            "occupation": occupation,
            "facts": facts,
            "image": im,
            "image_name": photo,
            "hidden": hidden}
    if (db.people.insert_one(person).inserted_id != 0):
        print (person['name'], "successfully added!")

#_________test for seeing if photo worked
    # pup = db.fs.files.find({'_id':im}) #find the photo for the person that just got inserted
    # for att in pup:
    #     p = att['filename']
    #os.system("open ../form_ui/static/{0}".format(photo)) #check to see if the photo uploads correctly

# def main():
# if __name__ == '__main__':
#     main()
