from flask import Flask, render_template
import jinja2
import requests

app = Flask(__name__)

response = requests.get("https://api.npoint.io/4ac9c32a945d3983ac66")
posts = response.json()
# for blog_post in posts:
#     number = blog_post["id"]
#     title = blog_post["title"]
#     subtitle = blog_post["subtitle"]
#     body = blog_post["body"]
@app.route('/')
def home_page():
    return render_template("index.html", posts=posts)

@app.route('/about')
def about_page():
    return render_template("about.html")

@app.route("/contact")
def contact_page():
    return render_template("contact.html")

@app.route("/post/<int:index>")
def show_post(index):
    for blog_post in posts:
        if blog_post["id"] == index:
            return render_template("post.html", post=blog_post)

app.run(debug=True)

