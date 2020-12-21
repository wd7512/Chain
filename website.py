from flask import (Flask, render_template, redirect,
                   url_for, request, session, flash)
import pandas as pd
from datetime import timedelta  ##new import
from flask_sqlalchemy import SQLAlchemy  ##new import
from werkzeug.security import generate_password_hash, check_password_hash

# Create the application instance
app = Flask(__name__, template_folder="templates")
# ------------------SETUP---------------------------
app.secret_key = "hello"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
# users is the name of the table we will be referencing
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # remove prints everytime db changes
app.permanent_session_lifetime = timedelta(minutes=5)
db = SQLAlchemy(app)  # setting new db
# --------------DATABASE CLASS-----------------------
class database(db.Model):  # inherit db.model attributes #represent user object in database
    id = db.Column("id", db.Integer, primary_key=True)
    # defining each object will have an ID, it will be an integer,, and we will reference all objects to this id
    # every single row will have a different ID
    name = db.Column(db.String(100))  # 100 char max str
    email = db.Column(db.String(100), unique=True)  # values can be float, boolean etc...
    password = db.Column(db.String(100))

@app.route('/login', methods=['GET', 'POST'])  # login page
def login():
    if request.method == 'POST':  # if button pressed
        email = request.form.get('email')
        password = request.form.get('password')
        #print("Email: ", email,"Password: ", password)
        user = database.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return render_template('login.html', title='Homepage')  # if the user doesn't exist or password is wrong, reload the page
        else:
            #print("Database Password is: ", user.password)
            flash('Welcome')
            return redirect(url_for('home'))
    return render_template('login.html', title='Homepage')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':  # if button pressed
        email = request.form.get('email')
        name = request.form.get('username')
        password = request.form.get('password')
        #print(email,name,password) # Prints 1,1,1
        user = database.query.filter_by(email=email).first()
        #print(user) # prints None
        if user:  # if a user is found, we want to redirect back to signup page so user can try again
            return redirect(url_for('login'))
        else:
            new_user = database(email=email, name=name,
                            password=generate_password_hash(password, method='sha256'))
            #print(new_user)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('signup.html', title='Homepage')


# Create a URL route in our application for "/"
@app.route('/')
def home():
    return render_template('home.html', title='Homepage')


@app.route('/contact')  # contact page
def contact():
    return render_template('contact.html', title='Contact')


@app.route('/test')
def test():
    return render_template('test.html')


@app.route("/database")
def view():
    return render_template("database.html", values = database.query.all()) #get all db users and pass them to the template


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)



# def signup():
#     success = None
#     if request.method == 'POST':  # if button pressed
#         with open('logins.csv', 'r') as login_data:  # open login data
#             df = pd.read_csv(login_data)
#
#         user_list = list(df['Username'])
#         input_user = request.form['username']
#         input_pass = request.form['password']
#
#         try:
#             u = user_list.index(input_user)  # locate username
#             success = 'Username already exists, please try another'
#
#         except ValueError:
#             with open('logins.csv', 'a') as login_data:  # open login data
#                 login_data.write('\n' + input_user + ',' + input_pass)
#             success = 'Account created with name: ' + input_user
#
#     return render_template('signup.html', title='SignUp', success=success)

# def login():
#     error = None
#     if request.method == 'POST':  # if button pressed
#         with open('logins.csv', 'r') as login_data:  # open login data
#             df = pd.read_csv(login_data)
#         input_user = request.form['username']
#         input_pass = request.form['password']
#         user_list = list(df['Username'])
#         pass_list = list(df['Password'])
#         try:
#             u = user_list.index(input_user)  # locate username
#             p = pass_list.index(input_pass)  # locate password
#             if u == p:  # check is match
#                 return redirect(url_for('home'))
#         except ValueError:  # if not found
#             pass
#         error = 'Invalid Credentials. Please try again.'
#     return render_template('login.html', error=error, title='Login')