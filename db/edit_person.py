import pymongo
import sys
import gridfs
import os


def editOne(id, name, degree, occupation, icon_filename, image1_filename, paragraph1,
                image2_filename, paragraph2, image3_filename, paragraph3, category, hidden): # school, year, occupation, facts, filename, hidden
	client = pymongo.MongoClient("mongodb+srv://erinruby:colorado18@yame-project-6ex3z.mongodb.net/test?retryWrites=true") #ERIN's LOGIN
	db = client.prototype #name of the db
	col = client.people #name of the collection
	fs = gridfs.GridFS(db)
	icon = fs.put(open('../form_ui/static/imj/{0}'.format(icon_filename), 'rb'), filename='{0}'.format(icon_filename)) #store the photo in the db
	image1 = fs.put(open('../form_ui/static/imj/{0}'.format(image1_filename), 'rb'), filename='{0}'.format(image1_filename)) #store the photo in the db
	image2 = fs.put(open('../form_ui/static/imj/{0}'.format(image2_filename), 'rb'), filename='{0}'.format(image2_filename)) #store the photo in the db
	image3 = fs.put(open('../form_ui/static/imj/{0}'.format(image3_filename), 'rb'), filename='{0}'.format(image3_filename)) #store the photo in the db

	person={"name":name,
	"subtitle":degree,
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

	db.people.update_one({"_id": id}, { "$set": person })
