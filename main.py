import requests
from flask import Flask, render_template, request, redirect
from bs4 import BeautifulSoup
from routes import routes
from twilio.rest import Client
from decouple import config


API_SID = config('SID')
API_TOKEN = config('TOKEN')
FROM_PHONE = config('FROM_PHONE')
TO_PHONE = config("TO_PHONE")

# autenticacao twilio
# pegue suas credenciais: http://twil.io/secure
account_sid = API_SID
auth_token = API_TOKEN
client = Client(account_sid, auth_token)

client.messages.create(
    to=TO_PHONE,
    from_=FROM_PHONE,
    body="O código de rastreio é: "
)


app = Flask("TwilioApi")


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/sent')
def sent():
    return render_template("sent.html")


app.run(host="0.0.0.0")
