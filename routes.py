from requests import request
from flask import Flask, render_template, request, redirect

def routes():
    app = Flask("TwilioApi")

    @app.route('/')
    def home():
        return render_template("index.html")

    @app.route('/sent')
    def sent():
        return render_template("sent.html")