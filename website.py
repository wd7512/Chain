from flask import (Flask, render_template,redirect,url_for, Markup, request)
from models import login_page, setup_db, signup_page, forgot_pass, open_table, auth_page
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

app = Flask(__name__, template_folder="templates")
setup_db(app)
# ---------------------------------------------------------


app.secret_key = "hello"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
# logins is the name of the table we will be referencing
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # remove prints everytime db changes
app.permanent_session_lifetime = timedelta(minutes=5)
db = SQLAlchemy(app)  # setting new db


class logins(db.Model):  # inherit db.model attributes #represent user object in logins
    id = db.Column("id", db.Integer, primary_key=True)
    # defining each object will have an ID, it will be an integer,, and we will reference all objects to this id
    # every single row will have a different ID
    name = db.Column(db.String(100))  # 100 char max str
    email = db.Column(db.String(100), unique=True)  # values can be float, boolean etc...
    password = db.Column(db.String(100))
    customer_type = db.Column(db.String(100))
    verified = db.Column(db.String(100))
    key = db.Column(db.String(100), unique=True)


class company(db.Model):  # inherit db.model attributes #represent user object in logins
    id = db.Column("id", db.Integer, primary_key=True)
    # defining each object will have an ID, it will be an integer,, and we will reference all objects to this id
    # every single row will have a different ID
    name = db.Column(db.String(100))  # 100 char max str


class ig_users(db.Model):  # inherit db.model attributes #represent user object in users
    id = db.Column("id", db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)  # values can be float, boolean etc...
    number_followers = db.Column(db.String(100))
    target_gender = db.Column(db.String(100))  # 100 char max str
    target_age = db.Column(db.String(100))
    product_preference = db.Column(db.String(100))
    instagram_account = db.Column(db.String(100))
    location = db.Column(db.String(100))


db.create_all()


@app.route("/signup/setup", methods=['GET', 'POST'])
def signupsetup():
    if request.method == 'POST':  # if button pressed
        email = request.args.get('email')
        number_followers = request.form.get("ig_followers_number")
        target_gender = request.form.get('target_audience_gender')
        target_age = request.form.get('target_audience_age')
        product_preference = request.form.get("product_preference")
        instagram_account = request.form.get("insta_account")
        location = request.form.get("location")
        print(email,number_followers,target_gender,target_age,product_preference,instagram_account,location)
        entry = ig_users(email=email,
                         number_followers=number_followers,
                         target_gender=target_gender,
                         target_age=target_age,
                         product_preference=product_preference,
                         instagram_account=instagram_account,
                         location=location)
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('home'))
        print("added entry to database")
    return render_template("ig_user_form.html", title="Home")


@app.route('/login', methods=['GET', 'POST'])  # login page
def login():
    return login_page()


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return signup_page()


# Create a URL route in our application for "/"
@app.route('/')
def home():
    return render_template('home.html', title='Homepage')


@app.route('/contact')  # contact page
def contact():
    return render_template('contact.html', title='Contact')


@app.route('/signup/auth', methods=['GET', 'POST'])  # authentication page
def auth():
    return auth_page()


@app.route('/passchange', methods=['GET', 'POST'])  # password change page
def passchange():
    return forgot_pass()


@app.route('/test')
def test():
    return render_template('test.html')


@app.route("/database")
def view():
    datafram = open_table('logins')
    return render_template("database.html",
                           values=Markup(datafram.to_html()))  # get all db users and pass them to the template


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)
    db.create_all()
