from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/')
def intro():
    return render_template('index.html')

@app.route('/register', methods=["POST"])
def registration():
    name = request.form.get('name')
    Gender = request.form.get('Gender')
    emailAddress = request.form.get('emailAddress')
    if not name or not Gender or not emailAddress:
        return render_template("failure.html")
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login("visheshsciensism@gmail.com", "ohyeah!!!!")
    msg = MIMEMultipart();
    msg['From'] = 'Vishesh Tayal'
    msg['To'] = 'YOLO'
    msg['subject'] = 'Greetings/Registration!'
    msg.attach(MIMEText("\nHello, " + name + "\n\tWe welcome you to the committee Congratulations for Making it till Here!! "))
    msg.as_string()
    server.sendmail("visheshsciensism@gmail.com", emailAddress, str(msg))
    print("The mail was Sent!!")
    return render_template("success.html")
    
