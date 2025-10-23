from flask import Flask
import tarot_gen.tarot_gen as tgen

app = Flask(__name__)


@app.route("/")
def hello_world():
    string = tgen.say_hi("Matt")
    return "<p>" + string + "</p>"
