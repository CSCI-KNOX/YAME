import pymongo
import sys
import gridfs
import os


def editOne(id, name, degree): # school, year, occupation, facts, filename, hidden
	client = pymongo.MongoClient("mongodb+srv://erinruby:colorado18@yame-project-6ex3z.mongodb.net/test?retryWrites=true") #ERIN's LOGIN
	db = client.prototype #name of the db
	col = client.people #name of the collection
	fs=gridfs.GridFS(db)
	if (db.Employees.update_one( {"id": id}, { "$set": { "name":name, "degree": degree }}) != 0):
		print (name, "successfully edited!")
