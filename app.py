from flask import Flask, send_file, render_template
import tarot_gen.tarot_gen as tgen
import os
import io
import base64

app = Flask(__name__, template_folder='templates')


@app.route("/")
def hello_world():
    stringa = tgen.say_hi("Matt")
    #return "<p>" + string + "</p>"
    print("File location using os.getcwd():", os.getcwd())

    tarot_base64 = tgen.get_tarot_base64()
    return render_template("index.html", person=stringa, img64=tarot_base64)

@app.route("/img")
def get_img():
    img_bytes = tgen.get_img()
    return send_file(img_bytes, mimetype='image/png')
    #return "<h3>Getting IMG...</h3>"
