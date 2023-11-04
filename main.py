from flask import Flask, render_template, url_for
app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(debug=True)
