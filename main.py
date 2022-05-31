import requests
from bs4 import BeautifulSoup
from twilio.rest import Client

# autenticacao twilio
# pegue suas credenciais: http://twil.io/secure
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

