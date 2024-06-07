from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

mail = Mail(app)

app.config['MAIL_SERVER']='live.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'api'
app.config['MAIL_PASSWORD'] = 'de01a2f1da2d2ce0fa9a83e1545129af'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

@app.route("/")
def index():
    msg = Message(subject='Hello from the other side!', sender='peter@mailtrap.io', recipients=['paul@mailtrap.io'])
    msg.body = "Hey Paul, sending you this email from my Flask app, lmk if it works."
    mail.send(msg)
    return "Message sent!"


if __name__ == '__main__':
    app.run(debug=True)
