# Code adapted from https://pythonspot.com/flask-web-forms/

import os
import pymongo
from flask import Flask, render_template, flash, request
from wtforms import Form, SelectField, TextField, TextAreaField, validators, StringField, SubmitField

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
        file = request.files['image']
        if file:
            f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(f)
        print (name, degree, occupation, file)

        if form.validate():
            flash(file.filename)
            os.system('cd ../db && python add_person.py {0} {1} {2} {3}'.format(name, degree, occupation, file.filename))
            print("upload to database successful")
        else:
            flash('All the form fields are required.')
    return render_template('hello.html', form=form)


@app.route("/people/", methods=['GET', 'POST'])
def people():

    client = pymongo.MongoClient("mongodb+srv://erinruby:colorado18@yame-project-6ex3z.mongodb.net/test?retryWrites=true") #ERIN's LOGIN
    db = client.prototype #name of the db
    col = client.people #name of the collection

    cursor = db.people.find({})
    personarr = []
    for att in cursor:
        n = att["name"]
        n = n.replace('+', ' ')
        print(n)
        personarr.append(n)
    return render_template('people.html', people = personarr)

if __name__ == "__main__":
    app.run()
