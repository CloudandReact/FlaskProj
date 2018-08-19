from app import app
from app.forms import LoginForm

from flask import render_template,redirect,flash, url_for
@app.route('/base')
def base():
    return render_template("base.html",title="Home Page")
# doesnt seem to matter what I put in the methods
@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print("attempting to login ")
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        print(url_for('index'))
        return redirect(url_for("index"))
    return render_template("login.html",title="Login Page",form=form)
@app.route('/')
@app.route('/index')
def index():
    user = {'username':'miguel'}
    posts = [
		{"author":"Jack", "body":"Batman good"},
		{"author":"Wayne", "body":"Avengers are good"}]
    return render_template('index.html', title='Home', user=user,posts=posts)
