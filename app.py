from flask import Flask, send_file, render_template, request
import tarot_gen.tarot_gen as tgen
import os
import io
import base64
import zipfile

app = Flask(
    __name__,
    template_folder='templates',
    static_folder='static')


@app.get("/draw")
@app.route("/")
def hello_world():
    stringa = tgen.say_hi("Matt")
    #return "<p>" + string + "</p>"
    print("File location using os.getcwd():", os.getcwd())

    tarot_base64 = tgen.get_tarot_base64()
    return render_template("index.html", person=stringa, img64=tarot_base64)


@app.route("/img")
def get_img():
    img_bytes = tgen.get_img()[0]
    return send_file(img_bytes, mimetype='image/png')
    #return "<h3>Getting IMG...</h3>"


@app.post("/draw")
def draw_cards():
    number_of_cards = int(request.form['card_number_select'])
    allow_reversals = request.form['reversals_select']
   
    # safety check
    if number_of_cards > 10:
        number_of_cards = 10
    elif number_of_cards < 1:
        number_of_cards = 1

    cards = []

    # These are all TUPLES (base64_img, alt_desc_text) that we're receiving
    for i in range(number_of_cards):
        img_id = "img_" + str(i)
        tarot_base64 = tgen.get_tarot_base64()
        cards.append((tarot_base64[0], tarot_base64[1], img_id))

    return render_template(
            "draw.html",
            number=number_of_cards,
            cards64=cards,
            allow_reversals=allow_reversals
        )


# package some images as PNGs in a zip file for the discord bot
@app.post("/discord")
def discord_req():
    number_of_cards = int(request.form['card_number_select'])

    if number_of_cards > 7:
        number_of_cards = 7
    elif number_of_cards < 1:
        number_of_cards = 1

    # create in-memory bytes buffer
    zip_buffer = io.BytesIO()

    # create a zip file object in write mode
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for i in range(number_of_cards):
            img_bytes = tgen.get_img()[0]
            zip_file.writestr(
                    f"image_{i + 1}.png",
                    img_bytes.getvalue()
                )
 
    zip_buffer.seek(0)

    return send_file(
            zip_buffer,
            mimetype='application/zip',
            as_attachment=True,
            download_name='cards.zip'
        )
