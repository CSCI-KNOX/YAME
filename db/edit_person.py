import pymongo
import sys
import gridfs
import os


def editOne(id, name, degree, school, ex, year, occupation, facts, photo, alt_txt, icon, hidden): # school, year, occupation, facts, filename, hidden
	client = pymongo.MongoClient("mongodb+srv://erinruby:colorado18@yame-project-6ex3z.mongodb.net/test?retryWrites=true") #ERIN's LOGIN
	db = client.prototype #name of the db
	col = client.people #name of the collection
	fs = gridfs.GridFS(db)
	im = fs.put(open('../form_ui/static/imj/{0}'.format(photo), 'rb'), filename='{0}'.format(photo)) #store the photo in the db
	ic = fs.put(open('../form_ui/static/imj/{0}'.format(photo), 'rb'), filename='{0}'.format(icon)) #store the photo in the db

	person = {"name": name,
			"degree": degree,
			"school": school,
			"ex": ex,
			"year": year,
			"occupation": occupation,
			"facts": facts,
			"image": im,
			"icon":ic,
			"icon_name": icon,
			"image_name": photo,
			"alt_txt": alt_txt,
			"hidden": hidden}
	db.people.update_one({"_id": id}, { "$set": {person}})
