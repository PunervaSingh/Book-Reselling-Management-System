from main import app
from flask import render_template, request
from main.models import Contact,Login,Register
from main import db

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if password == '' or email == '':
            return render_template('login.html', message='Please enter required field')
        data = Login(email,password)
        db.session.add(data)
        db.session.commit()
        return render_template('index.html', message='Login successfully')
    return render_template('login.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        state = request.form['state']
        city = request.form['city']
        password = request.form['password']
        c_password = request.form['c_password']
        if name == '' or password == '' or email=='' or state==''  :
            return render_template('register.html', message='Please enter required field')
        if password != c_password:
            return render_template('register.html', message="Passwords don't match")
        data = Register(name, email, state, city , password)
        db.session.add(data)
        db.session.commit()
        return render_template('index.html', message='You have been successfully registered')
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
