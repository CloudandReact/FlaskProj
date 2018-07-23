from app import app

from flask import render_template
@app.route('/base')
def base():
    return render_template("base.html",title="Home Page")
@app.route('/')
@app.route('/index')
def index():
    user = {'username':'miguel'}
    posts = [
		{"author":"Jack", "body":"Batman good"},
		{"author":"Wayne", "body":"Avengers are good"}]
    return render_template('index.html', title='Home', user=user,posts=posts)
