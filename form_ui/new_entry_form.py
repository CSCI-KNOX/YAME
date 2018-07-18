# Code adapted from https://pythonspot.com/flask-web-forms/

import os, sys
import datetime
import pymongo
import numpy as np
from flask import Flask, render_template, flash, request
from wtforms import Form, SelectField, TextField, TextAreaField, validators, StringField, SubmitField

#importing and using files from the db folder
sys.path.append('../db')
import retrieve_from_db, add_person, edit_person

# App config.
DEBUG = True
app = Flask(__name__)

app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

UPLOAD_FOLDER = 'static/imj'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def checkbox(id):
    try:
        value = request.form[id]
        value = 1
    except:
        value = 0
    return value

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
        ex = checkbox('ex')
        occupation=request.form['occupation']
        facts=request.form['facts']
        file = request.files['image']
        alt_txt = request.form['alt_txt']
        hidden = checkbox('hidden')
        if file:
            f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(f)
            filename = file.filename
        # Use default photo
        else:
            filename = 'default.jpg'
        if form.validate():
            flash(filename)
            add_person.addOne(name, degree, school, ex, year, occupation, facts, filename, alt_txt, hidden)
            print("upload to database successful")
        else:
            flash('All the form fields are required.')
    return render_template('hello.html', form=form)


@app.route("/people/", methods=['GET', 'POST'])
def people():
    form = ReusableForm(request.form)
    personarr = retrieve_from_db.getAll() #returns all people in the database
    personarr.sort()
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    # letter = request.form['name']
    # print (letter)
    # person = retrieve_from_db.searchByLetter(letter)
    return render_template('people.html', person = person, people = personarr, alphabet=alphabet)


@app.route("/edit/", methods=['GET', 'POST'])
def edit():
    form = ReusableForm(request.form)
    name = request.args.get('name')
    person = retrieve_from_db.getOneforDisplay(name)
    if request.method == 'POST':
        name=request.form['name']
        degree=request.form['degree']
        school=request.form['school']
        year=request.form['year']
        ex = checkbox('ex')
        occupation=request.form['occupation']
        facts=request.form['facts']
        file = request.files['image']
        alt_txt = request.form['alt_txt']
        hidden = checkbox('hidden')
        if file:
            f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(f)
            filename = file.filename
        else:
            filename = person['image_name']
        if form.validate():
            flash(person['name'])
            edit_person.editOne(person['_id'], name, degree, school, ex, year, occupation, facts, filename, alt_txt, hidden)
            print("edit to database successful")
        else:
            flash('All the form fields are required.')
    return render_template('edit.html', person=person, form=form)


@app.route("/person/", methods=['GET', 'POST'])
def person():
    name = request.args.get('name')
    person = retrieve_from_db.getOneforDisplay(name)
    return render_template('person.html', person=person)


@app.route("/display/", methods=['GET', 'POST'])
def display():
    # name = request.args.get('name')
    # if name==None:
    #     personarr = retrieve_from_db.getAll()
    #     name = np.random.choice(personarr)
    # person = retrieve_from_db.getOneforDisplay(name)
    personarr = retrieve_from_db.getAllContent()
    return render_template('display.html', personarr=personarr) # person=person

@app.route("/search/", methods=['GET', 'POST'])
def search():
    form = ReusableForm(request.form)
    print (form.errors)
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    person = []
    toFind = {}
    if request.method == 'POST':
        try:
            letter = request.form['name']
            print (letter)
            person = retrieve_from_db.searchByLetter(letter)
        except:
            toFind['name'] = ''
        try:
            toFind['school'] = request.form['school']
            person = retrieve_from_db.getOne(toFind)
        except:
            toFind['school'] = ''
        try:
            toFind['year'] = request.form['year']
            person = retrieve_from_db.getOne(toFind)
        except:
            toFind['year'] = ''
    # person = retrieve_from_db.getOne(toFind)
    return render_template('search.html', form=form, person=person, alphabet=alphabet)


if __name__ == "__main__":
    app.run()
