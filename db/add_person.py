import pymongo
import sys
import gridfs
import os
#hello
#example: python add_person.py erin cs student
def addOne(name, degree, occupation, icon_filename, image1_filename, paragraph1,
                image2_filename, paragraph2, image3_filename, paragraph3, category, hidden):
    client = pymongo.MongoClient("mongodb+srv://erinruby:colorado18@yame-project-6ex3z.mongodb.net/test?retryWrites=true") #ERIN's LOGIN
    db = client.prototype #name of the db
    col = client.people #name of the collection

    fs=gridfs.GridFS(db)
    icon = fs.put(open('../form_ui/static/imj/{0}'.format(icon_filename), 'rb'), filename='{0}'.format(icon_filename)) #store the photo in the db
    image1 = fs.put(open('../form_ui/static/imj/{0}'.format(image1_filename), 'rb'), filename='{0}'.format(image1_filename)) #store the photo in the db
    image2 = fs.put(open('../form_ui/static/imj/{0}'.format(image2_filename), 'rb'), filename='{0}'.format(image2_filename)) #store the photo in the db
    image3 = fs.put(open('../form_ui/static/imj/{0}'.format(image3_filename), 'rb'), filename='{0}'.format(image3_filename)) #store the photo in the db


    person = {"name": name,
            "subtitle": degree,
            "heading": occupation,
            "icon": icon,
            "image1": image1,
            "paragraph1": paragraph1,
            "image2": image2,
            "paragraph2": paragraph2,
            "image3": image3,
            "paragraph3": paragraph3,
            "category":category,
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
