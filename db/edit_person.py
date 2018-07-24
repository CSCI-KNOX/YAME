import pymongo
import sys
import gridfs
import os


def editOne(id, name, degree, occupation, icon_filename, image1_filename, paragraph1,
                image2_filename, paragraph2, image3_filename, paragraph3, category, hidden, iscategory): # school, year, occupation, facts, filename, hidden
	client = pymongo.MongoClient("mongodb+srv://erinruby:colorado18@yame-project-6ex3z.mongodb.net/test?retryWrites=true") #ERIN's LOGIN
	db = client.prototype #name of the db
	col = client.people #name of the collection
	fs = gridfs.GridFS(db)
	im = fs.put(open('../form_ui/static/imj/{0}'.format(photo), 'rb'), filename='{0}'.format(photo)) #store the photo in the db

	person={"name":name,
	"degree":degree,
            "occupation": occupation,
            "icon": icon,
            "image1": image1,
            "paragraph1": paragraph1,
            "image2": image2,
            "paragraph2": paragraph2,
            "image3": image3,
            "paragraph3": paragraph3,
            "category":category,
            "hidden": hidden,
            "iscategory": iscategory}

	db.people.update_one({"_id": id}, { "$set": person })
