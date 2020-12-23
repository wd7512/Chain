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


def setup_db(app):
    global db  # make variables accessible
    global users

    app.secret_key = "hello"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
    # users is the name of the table we will be referencing
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # remove prints everytime db changes
    app.permanent_session_lifetime = timedelta(minutes=5)
    db = SQLAlchemy(app)  # setting new db

    class users(db.Model):  # inherit db.model attributes #represent user object in users
        id = db.Column("id", db.Integer, primary_key=True)
        # defining each object will have an ID, it will be an integer,, and we will reference all objects to this id
        # every single row will have a different ID
        name = db.Column(db.String(100))  # 100 char max str
        email = db.Column(db.String(100), unique=True)  # values can be float, boolean etc...
        password = db.Column(db.String(100))
        customer_type = db.Column(db.String(100))

    db.create_all()

    return users


def login_page():
    if request.method == 'POST':  # if button pressed
        email = request.form.get('email')
        password = request.form.get('password')
        user = users.query.filter_by(email=email).first()
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
        user = users.query.filter_by(email=email).first()
        # print(user) # prints None
        if user:  # if a user is found, we want to redirect back to signup page so user can try again
            return redirect(url_for('login'))
        else:
            new_user = users(email=email, name=name,
                             password=generate_password_hash(password, method='sha256'),
                             customer_type=input_customer_type)
            # print(new_user)
            flash("New customer: ", f"{email, name, password, input_customer_type}")
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('signup.html', title='Homepage')


def forgot_pass():
    if request.method == 'POST':
        email = request.form.get('email')
        user = users.query.filter_by(email=email).first()
        if user:  # if a user is found, we want to redirect back to signup page so user can try again
            send_email(email, 'changepass')
        else:
            return redirect(url_for('passchange'))

    return render_template('passchange.html', title='Change Password')
