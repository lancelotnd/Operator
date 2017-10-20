from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def welcome():
    resp = VoiceResponse()
    resp.say("Welcome Lancelot")

    return str(resp)

if __name__ == "__main__":
    app.run()
