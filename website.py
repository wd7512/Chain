from flask import (Flask, render_template, Markup)
from models import login_page, setup_db, signup_page, forgot_pass, open_table
from alembic import op # For Database migrations
# Create the application instance
app = Flask(__name__, template_folder="templates")
users = setup_db(app)
datafram = open_table('users')





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


@app.route('/auth')  # authentication page
def auth():
    return render_template('auth.html', title='Auth')


@app.route('/passchange', methods=['GET', 'POST'])  # password change page
def passchange():
    return forgot_pass()


@app.route('/test')
def test():
    return render_template('test.html')


@app.route("/database")
def view():
    return render_template("database.html",
                           values=Markup(datafram.to_html()))  # get all db users and pass them to the template


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)
