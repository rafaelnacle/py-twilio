from twilio.rest import Client
from decouple import config


def twilio_msg(phone, body):
    API_SID = config('SID')
    API_TOKEN = config('TOKEN')
    FROM_PHONE = config('FROM_PHONE')

    # autenticacao twilio
    # pegue suas credenciais: http://twil.io/secure
    account_sid = API_SID
    auth_token = API_TOKEN
    client = Client(account_sid, auth_token)

    client.messages.create(
        to=phone,
        from_=FROM_PHONE,
        body=body
    )
