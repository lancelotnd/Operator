from flask import Flask
from twilio.twiml.voice_response import Conference, Dial, VoiceResponse
from twilio.rest import Client

account_sid = "AC190046e06b0612f0f1be5beab91f7030"
auth_token = "a0e68c354c1a4d54021a99800a031040"
client = Client(account_sid, auth_token)

app = Flask(__name__)


@app.route("/voice", methods=['GET', 'POST'])
def conference():
    response = VoiceResponse()
    dial = Dial()
    dial.conference('Room 1234')
    response.append(dial)

    return str(response)


if __name__ == "__main__":
    app.run()
