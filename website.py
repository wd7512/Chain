from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    request
)
import pandas as pd
######################
# Create the application instance
app = Flask(__name__, template_folder="templates")

# Create a URL route in our application for "/"
@app.route('/')
def home():
    return render_template('home.html',title='Homepage')
    
@app.route('/contact') #contact page
def contact():
    return render_template('contact.html',title='Contact')
    
@app.route('/login', methods=['GET', 'POST']) #login page
def login():
    error = None
    if request.method == 'POST': #if button pressed
        with open('logins.csv','r') as login_data: #open login data
            df = pd.read_csv(login_data)
        input_user = request.form['username']
        input_pass = request.form['password']
        user_list = list(df['Username'])
        pass_list = list(df['Password'])
        try:
            u = user_list.index(input_user) #locate username
            p = pass_list.index(input_pass) #locate password
            if u==p: #check is match
                return redirect(url_for('/'))
        except ValueError: #if not found
            pass
        error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error=error,title='Login')
    
@app.route('/signup', methods=['GET', 'POST']) 
def signup():
    success = None
    if request.method == 'POST': #if button pressed
        with open('logins.csv','r') as login_data: #open login data
            df = pd.read_csv(login_data)
        with open('logins.csv','a') as login_data: #open login data
            user_list = list(df['Username'])
            input_user = request.form['username']
            input_pass = request.form['password']
            
            try:
                u = user_list.index(input_user) #locate username
                success='Username already exists, please try another'

            except ValueError:
                login_data.write('\n'+input_user+','+input_pass)
                success = 'Account created with name: ' + input_user


    return render_template('signup.html',title='SignUp',success=success)

@app.route('/test')
def test():
    return render_template('test.html')

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)
