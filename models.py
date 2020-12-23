import smtplib, ssl
from datetime import timedelta  ##new import
from flask_sqlalchemy import SQLAlchemy  ##new import
from sqlalchemy import Column, String,Integer, Unicode, engine
from werkzeug.security import generate_password_hash, check_password_hash
from flask import (Flask, render_template, redirect,
                   url_for, request, session, flash)
import pandas as pd
import sqlite3
from alembic import op # For Database migrations
import random


def open_table(table_name):
    # Create your connection.
    cnx = sqlite3.connect('database.sqlite3')
    df = pd.read_sql_query('SELECT * FROM ' + table_name, cnx)
    return df


def send_email(receiver_email, message):
    port = 465  # For SSL
    password = 'bath2020'
    sender_email = 'chain.app.ai@gmail.com'

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        
    #print('email sent to:'+receiver_email)
    #print('message:'+message)


def setup_db(app):
    global db  # make variables accessible
    global logins

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
        key = db.Column(db.String(100),unique=True)


    class company(db.Model):  # inherit db.model attributes #represent user object in logins
        id = db.Column("id", db.Integer, primary_key=True)
        # defining each object will have an ID, it will be an integer,, and we will reference all objects to this id
        # every single row will have a different ID
        name = db.Column(db.String(100))  # 100 char max str

    class ig_users_data(db.Model):  # inherit db.model attributes #represent user object in users
        id = db.Column("id", db.Integer, primary_key=True)
        email = db.Column(db.String(100), unique=True)  # values can be float, boolean etc...
        customer_type = db.Column(db.String(100))
        instagram_name = db.Column(db.String(100))  # 100 char max str
        target_audience = db.Column(db.String(100))
        location = db.Column(db.String(100))
        followers = db.Column(db.Integer)
        product_preference = db.Column(db.String(100))
        age = db.Column(db.Integer)
        gender = db.Column(db.String(100))

        
        
    db.create_all()



def login_page():
    if request.method == 'POST':  # if button pressed
        email = request.form.get('email')
        password = request.form.get('password')
        user = logins.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return render_template('login.html',
                                   title='Homepage')  # if the user doesn't exist or password is wrong, reload the page
        else:
            # print("Database Password is: ", user.password)
            flash('Welcome')
            return redirect(url_for('home'))
    return render_template('login.html', title='Homepage')


def signup_page():
    if request.method == 'POST':  # if button pressed
        email = request.form.get('email')
        name = request.form.get('username')
        password = request.form.get('password')
        input_customer_type = request.form.get("customer_type")
        print(email, name, password, input_customer_type)  # Prints 1,1,1
        user = logins.query.filter_by(email=email).first()
        # print(user) # prints None
        if user:  # if a user is found, we want to redirect back to signup page so user can try again
            return redirect(url_for('login'))
        else:
            key = random.randint(100000,999999)
            while logins.query.filter_by(key=key).first(): # if code already used
                key = random.randint(100000,999999)

            send_email(email,'To authenticate account please type in this code '+str(key))
            new_user = logins(email=email, name=name,
                             password=generate_password_hash(password, method='sha256'),
                             customer_type=input_customer_type,verified=0,key=key)
            # print(new_user)
            flash("New customer: ", f"{email, name, password, input_customer_type}")
            db.session.add(new_user)
            db.session.commit()
            
            
            return redirect(url_for('auth'))
            
    return render_template('signup.html', title='Homepage')


def forgot_pass():
    if request.method == 'POST':
        email = request.form.get('email')
        user = logins.query.filter_by(email=email).first()
        if user:  # if a user is found, we want to redirect back to signup page so user can try again
            send_email(email, 'changepass')
        else:
            return redirect(url_for('passchange'))

    return render_template('passchange.html', title='Change Password')
    
def auth_page():
    if request.method == 'POST':
        code = request.form.get('code')
        user = logins.query.filter_by(key=code).first()
        if user:
            user.verified = 1
            user.key = 'null'
            db.session.commit()
            flash('Verified: '+ str(user))
        else:
            flash('Incorrect Code')
        
    return render_template('auth.html', title='Auth')
