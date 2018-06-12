# Code adapted from https://pythonspot.com/flask-web-forms/

import os, sys
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
        name=request.form['name'].replace(' ', '+')+' ' # key value pairs
        degree=request.form['degree'].replace(' ', '+')+' '
        occupation=request.form['occupation'].replace(' ', '+')+' '
        school=request.form['school']+' '
        facts=request.form['facts'].replace(' ', '+')+' '
        file = request.files['image']
        if file:
            f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(f)
        print (name, degree, occupation, file)

        if form.validate():
            flash(file.filename)
            add_person.addOne(name, degree, occupation, file.filename)
            # os.system('cd ../db && python add_person.py {0} {1} {2} {3}'.format(name, degree, occupation, file.filename))
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
    person = retrieve_from_db.getOne('erin ruby')
    # person = {}
    # person['name'] = 'Test Person'
    # person['birthday'] = 122297
    # person['school'] = 'CU'
    # person['degree'] = 'Computer Science'
    # person['occupation'] = 'Student'
    return render_template('edit.html', person=person, form=form)

if __name__ == "__main__":
    app.run()
