from flask import render_template, url_for, flash, redirect
from webapp import app
from webapp.forms import RegistrationForm, LoginForm
from webapp.models import User, Post


posts = [
    {
        'author': 'John Marquardt',
        'title': 'Why Blogs Are Garbo',
        'content': 'Reasons are not important.',
        'date_posted': 'April 20, 2020'
    },
    {
        'author': 'Grace Marquardt',
        'title': 'Why Buns Are Cute',
        'content': 'There are so many reasons.',
        'date_posted': 'April 21 2020'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password.', 'danger')
    return render_template('login.html', title='Login', form=form)

