from flask import Flask, render_template
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET KEY'] = ''

posts = [
    {
        'Author': 'Saurav Vishal',
        'Title': 'My journey with Flask',
        'Content': 'This is a dummy blog post intended for checking the working of the ap'
                   'p'
    },
    {
        'Author': 'Raj Malhorta',
        'Title': 'Has to be someone',
        'Content': 'Ploppy is the new San Fernandino to my state of Kansas'
    },
    {
        'Author': 'Sakuni Jajab',
        'Title': 'The take of the Mahabharata',
        'Content': 'The war of the Mahabharata has a special significance '
                   'in the mythological history of Republic of India'
    }
]

@app.route("/")
@app.route("/home")
def index():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title="About Page")

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(port=9900, debug=True)
