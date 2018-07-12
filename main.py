from flask import Flask, request, redirect, render_template, session, url_for

app = Flask(__name__)
app.config['DEBUG'] = True

# Declare global 'username' variable
username = ""

@app.route('/')
def index():
    app.secret_key = 'SDHFH(*#R&*(DGVFHNSDFJLHSDKHFJLDHJSF*(ASD^&F)DY*USHN'
    return render_template('base.html',title="User Signup")

@app.route('/submit', methods=['POST'])
def submit_credentials():
    # Process Username.
    username=request.form['username']
    username = session['username'] 
    username_error = ""

    # Verify if Username is correct...
    if username == "" or len(username)  < 3 or len(username) > 20:
        username_error = "That's not a valid username"

    # Process Password.
    password=request.form['password'] 
    password_error = ""

    # Verify if password is correct...
    if password == "" or len(password) < 5 or len(password) > 20 or password.count(" ") != 0:
        password_error = "That's not a valid password"

    # Process password re-entry.
    verify_password=request.form['verify_password']
    password_verify_error = ""

    # Verify password re-entry valid...
    if verify_password != password or verify_password == "":
        password_verify_error = "Passwords don't match"

    # Process email address.
    email=request.form['email'] 
    email_error = ""

    # Verify (optional) email address valid...
    if email != "":
        if len(email) < 3 or len(email) > 20 or email.count(" ") != 0 or email.count("@") != 1 or email.count(".") != 1:
           email_error = "Invalid email address"
        
    # Render some templates.
    if not password_error and not username_error and not password_error and not password_verify_error and not email_error:
        return redirect('/welcome')
    else:
        return render_template('base.html', username=username, username_error=username_error, 
             password_error=password_error, password_verify_error=password_verify_error, email=email, 
             email_error=email_error)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html',username=username)

app.run()
