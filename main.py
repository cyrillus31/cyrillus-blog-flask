import flask
from flask import Flask, render_template, url_for 
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '9efc17d27f6b28690111ebc0e4cf7c2e'

posts = [
        {
            "author": "Kirill Fedtsov",
            "title": "My test blog post",
            "content": "Here I talk about BJJ, computer programming, web, python, etc.",
            "date_posted": "November 4th, 2023",
            },
        {
            "author": "Grigoiry Fedtsov",
            "title": "Being a younger brother",
            "content": "I hope to become as skilled as my older brother in the future",
            "date_posted": "November 5th, 2023",
            }

        ]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts) 


@app.route("/about")
def about():
    return render_template("about.html", title='About')


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flask.flash(f"Account created for {form.username.data}!", category="success")
        return flask.redirect(url_for("home"))
    return render_template("register.html", title="Registration", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flask.flash(f"Successfully logged in as {form.email.data}!", category="success")
        return flask.redirect(url_for("home"))
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)
