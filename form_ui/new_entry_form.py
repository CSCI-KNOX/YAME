# Code adapted from https://pythonspot.com/flask-web-forms/

import os
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
 
# App config.
DEBUG = True
app = Flask(__name__)

app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
 
class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    degree = TextField('Degree or Faculty/Staff:', validators=[validators.required()])
    industry = TextField('Occupation or industry:', validators=[validators.required()])

 
@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
 
    print (form.errors)
    if request.method == 'POST':
        name=request.form['name'] # key value pairs
        degree=request.form['degree']
        industry=request.form['industry']
        file = request.files['image']
        f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(f)
        print (name, " ", degree, " ", industry)
 
        if form.validate():
            # Save the comment here.
            flash('Thank you for your upload of ' + file.filename + '.')
        else:
            flash('All the form fields are required. ')

    # system(run another python program, arguments as key value pairs)
 
    return render_template('hello.html', form=form)
 
if __name__ == "__main__":
    app.run()
