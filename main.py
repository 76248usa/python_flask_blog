from flask import Flask, render_template, request
import jinja2
import smtplib
import requests

EMAIL = "elsabecrous@gmail.com"
PASSWORD = "Gerhard987!Gerhard987!"

app = Flask(__name__)

response = requests.get("https://api.npoint.io/4ac9c32a945d3983ac66")
posts = response.json()
# for blog_post in posts:
#  number = blog_post["id"]
#  title = blog_post["title"]
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

@app.route('/login', methods=["POST"])
def receive_data():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    message = request.form["message"]
    return render_template("data_received.html", name=name, email=email, phone=phone, message=message)


@app.route("/post/<int:index>")
def show_post(index):
    for blog_post in posts:
        if blog_post["id"] == index:
            return render_template("post.html", post=blog_post)

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(EMAIL, EMAIL, email_message)
app.run(debug=True)

