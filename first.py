from flask import Flask, render_template, redirect, request, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message

app = Flask(__name__)


app.secret_key = "thisisthemostsecretkeyever"
app.config.update(
    DEBUG=True,
    # EMAIL SETTINGS
    MAIL_SERVER="smtp.gmail.com",
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME="cybercityy.ks@gmail.com",
    MAIL_PASSWORD="kosova22",
)
mail = Mail(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.route("/", methods=["POST", "GET"])
@app.route("/home", methods=["POST", "GET"])
def home():
    return render_template("index.html")



@app.route("/prove", methods=["POST", "GET"])
def prove():
    return render_template("prove.html")



@app.route("/contactus", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        lastname = request.form["last-name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        msg = Message(
                name + " " + lastname,
                sender="cybercityy.ks@gmail.com",
                recipients=["cybercityy.ks@gmail.com"],)
        msg.body = "Greetings"
        msg.html = render_template(
                "contactmsg.html", name=name, lastname=lastname, email=email, phone=phone, message=message
                  )
        mail.send(msg)
            

    return render_template("contactus.html")

if __name__ == "__main__":
    app.run(debug=True)
