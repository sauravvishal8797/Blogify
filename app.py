from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'd74306e39550f79330dbd2e530d4beae'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	profile_picture = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(60), nullable=False)
	posts = db.relationship('Post', backref='author', lazy=True)

	def __repr__(self):
		return f"User('{ self.username }', '{ self.email }', '{ self.profile_picture }')"


class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	date_posted = db.Column(db.Date, nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return f"Post('{ self.title }', '{ self.date_posted }', '{ self.content }')"

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

if __name__ == '__main__':
	app.run(port=9900,debug=True)

