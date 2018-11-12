from flask import redirect, render_template, flash, url_for
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flaskblog import app


posts = [
	{
		'title': 'Blog post 1',
		'author': 'Saurav Vishal',
		'date': '21st of July',
		'content': 'First blog post'
	},
	{
		'title': 'Blog post 2',
		'author': 'David Malan',
		'date': '21st of June',
		'content': 'Second blog post'
	},
	{
		'title': 'Blog post 3',
		'author': 'David J Malan',
		'date': '21st of June',
		'content': '3rd blog post'
	}
]


@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', posts = posts)

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for user {form.userName.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', form=form, title='Register')

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.userEmail.data == "sauravvishal8797@gmail.com" and form.password.data == "alala":
			flash("User succesfully logged in", "success")
			return redirect(url_for('home'))
		else:
			flash("Login Unsuccessful", "danger")
	return render_template('login.html', form=form, title="Login Here")
