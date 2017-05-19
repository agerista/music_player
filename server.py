"""music_player - twilio, spotify, musixmatch"""

import os
from flask import Flask, jsonify, render_template, redirect, request, Response, flash, session
from datetime import date
from twilio import twiml
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse, Gather
from jinja2 import StrictUndefined

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("FLASK_SECRET_KEY", "!y7ic$$4n9m0si2")
app.jinja_env.endefined = StrictUndefined


@app.route("/")
def index():
    """shows homepage"""

    return "Hello World!"


@app.route("/lyrics", methods=['GET', 'POST'])
def lyrics_reader():
    """Reads song lyrics to a user"""

    caller = "Silly Monkey"
    response = VoiceResponse()
    response.say("Hello" + caller)

    g = Gather(timeout="15", numDigits=5, action="/handle-key", method="POST")
    g.say("""Please enter the a song title""")

    response.append(g)

    return str(response)


@app.route("/handle-key", methods=['GET', 'POST'])
def lyrics_menu():
    """Handle key press from a user."""

    digit_pressed = request.values.get('Digits', None)
    if digit_pressed == "12345":

        resp = VoiceResponse()
        resp.say("Gathering information to read those lyrics to you")

        return str(resp)

################################################################################
if __name__ == "__main__":

    DEBUG = "NO_DEBUG" not in os.environ
    PORT = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=PORT)
