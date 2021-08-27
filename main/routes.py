from main import app
from flask import render_template, request
from main.models import Contact
from main import db

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/register", methods=['GET'])
def register():
    return render_template('register.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/addbook")
def addbook():
    return render_template('addbook.html')

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        msg = request.form['msg']
        if name == '' or email == '':
            return render_template('contact.html', message='Please enter required field')
        data = Contact(name, email, msg)
        db.session.add(data)
        db.session.commit()
        return render_template('index.html', message='Inquer message has been sent successfully...')
    return render_template('contact.html')

@app.route("/profile")
def profile():
    return render_template('profile.html')

@app.route("/singlepost")
def singlepost():
    return render_template('singlepost.html')
