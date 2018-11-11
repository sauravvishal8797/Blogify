from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'd74306e39550f79330dbd2e530d4beae'
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
	return render_template('login.html', form=form, title="Login Here")

if __name__ == '__main__':
	app.run(port=9900,debug=True)

