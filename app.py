from flask import Flask, send_file
import tarot_gen.tarot_gen as tgen

app = Flask(__name__)


@app.route("/")
def hello_world():
    string = tgen.say_hi("Matt")
    return "<p>" + string + "</p>"

@app.route("/img")
def get_img():
    img_bytes = tgen.get_img()
    return send_file(img_bytes, mimetype='image/png')
    #return "<h3>Getting IMG...</h3>"
