# Code adapted from https://pythonspot.com/flask-web-forms/

import os, sys
import datetime
import pymongo
from flask import Flask, render_template, flash, request
from wtforms import Form, SelectField, TextField, TextAreaField, validators, StringField, SubmitField

#importing and using files from the db folder
sys.path.append('../db')
import retrieve_from_db, add_person

# App config.
DEBUG = True
app = Flask(__name__)

app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

UPLOAD_FOLDER = os.path.basename('static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

class ReusableForm(Form):
    name = TextField('Name:')
    degree = TextField('Degree or Faculty/Staff:') #, validators=[validators.required()]
    occupation = TextField('Occupation or industry:')


@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)

    print (form.errors)
    if request.method == 'POST':
        name=request.form['name'] # key value pairs
        degree=request.form['degree']
        school=request.form['school']
        year=request.form['year']
        occupation=request.form['occupation']
        facts=request.form['facts']
        file = request.files['image']
        # If the user put in a photo
        if file:
            f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(f)
            filename = file.filename
        # Use default photo
        else:
            filename = 'default.jpg'
        if form.validate():
            flash(filename)
            add_person.addOne(name, degree, school, year, occupation, facts, filename)
            print("upload to database successful")
        else:
            flash('All the form fields are required.')
    return render_template('hello.html', form=form)


@app.route("/people/", methods=['GET', 'POST'])
def people():

    personarr = retrieve_from_db.getAll() #returns all people in the database
    return render_template('people.html', people = personarr)


@app.route("/edit/", methods=['GET', 'POST'])
def edit():
    form = ReusableForm(request.form)
    # instead of using this dictionary, get the info from the database into a dictionary.
    name = request.args.get('name')
    person = retrieve_from_db.getOne(name)
    return render_template('edit.html', person=person, form=form)


@app.route("/person/", methods=['GET', 'POST'])
def person():
    name = request.args.get('name')
    print(name)
    person = retrieve_from_db.getOne(name)
    return render_template('person.html', person=person)


@app.route("/display/", methods=['GET', 'POST'])
def display():
    name = request.args.get('name')
    person = retrieve_from_db.getOne(name)
    return render_template('display.html', person=person)

if __name__ == "__main__":
    app.run()
