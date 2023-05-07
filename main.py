import re

import speech_recognition as sr
from flask import Flask, render_template, request, session, redirect
from model import charToArray, asciicodes, brailles
import os
import logging
from base64 import b64encode

from flask_babelex import Babel, lazy_gettext
from flask_wtf import FlaskForm, CSRFProtect
from flask_wtf.file import FileField, FileRequired, FileAllowed

from ml.utils import Utils


app = Flask(__name__)
csrf = CSRFProtect(app)
babel = Babel(app)
app.config["SECRET_KEY"] = "xxxxx"
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024  # 10MB max for file upload
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)

class UploadForm(FlaskForm):
    """
    TODO: Display validation error messages clearly
    """
    photo = FileField(lazy_gettext("photo"), validators=[
        FileRequired(),
        FileAllowed(['jpeg', 'jpg', 'png'], lazy_gettext("Please upload image file"))
    ])

@app.route('/convert-audio', methods=['POST'])
def convertaudio():
    # use SpeechRecognition to convert the audio input to text
    recognizer = sr.Recognizer()
    audio = sr.AudioFile(request.files['audio'])

    with audio as source:
        audio_data = recognizer.record(source)
    speech_text = recognizer.recognize_google(audio_data)
    # use PyBraille to convert the text to Braille
    braille_text = convertwithargument(speech_text)

    # return the Braille text to the user
    return render_template('output.html', output=braille_text)

def convertwithargument(speech_text):
    ascii_braille = {}

    arrayLength = len(asciicodes)
    counter = 0

    while counter < arrayLength:
        ascii_braille[asciicodes[counter]] = brailles[counter]
        counter = counter + 1
    
    text = speech_text
    final_string = ''
    for char in text:
        char = char.lower()
        if char == "a":
            final_string = final_string + ascii_braille[char]
        elif char == "b":
            final_string = final_string + ascii_braille[char]
        elif char == "c":
            final_string = final_string + ascii_braille[char]
        elif char == "d":
            final_string = final_string + ascii_braille[char]
        elif char == "e": 
            final_string = final_string + ascii_braille[char]
        elif char == "f": 
            final_string = final_string + ascii_braille[char]
        elif char == "g":
            final_string = final_string + ascii_braille[char] 
        elif char == "h": 
            final_string = final_string + ascii_braille[char]
        elif char == "i":
            final_string = final_string + ascii_braille[char] 
        elif char == "j": 
            final_string = final_string + ascii_braille[char]
        elif char == "k": 
            final_string = final_string + ascii_braille[char]
        elif char == "l": 
            final_string = final_string + ascii_braille[char]
        elif char == "m": 
            final_string = final_string + ascii_braille[char]
        elif char == "n": 
            final_string = final_string + ascii_braille[char]
        elif char == "o":
            final_string = final_string + ascii_braille[char]
        elif char == "p": 
            final_string = final_string + ascii_braille[char]
        elif char == "q": 
            final_string = final_string + ascii_braille[char]
        elif char == "r": 
            final_string = final_string + ascii_braille[char]
        elif char == "s": 
            final_string = final_string + ascii_braille[char]
        elif char == "t": 
            final_string = final_string + ascii_braille[char]
        elif char == "u": 
            final_string = final_string + ascii_braille[char]
        elif char == "v": 
            final_string = final_string + ascii_braille[char]
        elif char == "w":
            final_string = final_string + ascii_braille[char] 
        elif char == "x": 
            final_string = final_string + ascii_braille[char]
        elif char == "y": 
            final_string = final_string + ascii_braille[char]
        elif char == "z":
            final_string = final_string + ascii_braille[char]
        elif char == " ":
            final_string = final_string + ascii_braille[char]
    return final_string

@app.route('/', methods=["GET", "POST"])
def main_page():
    form = UploadForm()
    output = None
    file_ext = None
    filename = None
    if form.validate_on_submit():
        image_binary = form.photo.data.read()
        file_ext = Utils.mimetype2ext(form.photo.data.mimetype)
        tactile_image_binary = Utils.photo2tactile(image_binary, file_ext)
        filename = "{}_converted".format(Utils.remove_file_ext(form.photo.data.filename))
        b64_binary = b64encode(tactile_image_binary)
        # Convert to string
        output = b64_binary.decode('utf8')
    return render_template(
        "index.html",
        form=form,
        output=output,
        file_ext=file_ext,
        filename=filename
    )

@app.route('/convert-to-braille', methods=['POST'])
def convert():
    ascii_braille = {}

    arrayLength = len(asciicodes)
    counter = 0

    while counter < arrayLength:
        ascii_braille[asciicodes[counter]] = brailles[counter]
        counter = counter + 1
    
    text = request.form['text']
    final_string = ''
    for char in text:
        char = char.lower()
        if char == "a":
            final_string = final_string + ascii_braille[char]
        elif char == "b":
            final_string = final_string + ascii_braille[char]
        elif char == "c":
            final_string = final_string + ascii_braille[char]
        elif char == "d":
            final_string = final_string + ascii_braille[char]
        elif char == "e": 
            final_string = final_string + ascii_braille[char]
        elif char == "f": 
            final_string = final_string + ascii_braille[char]
        elif char == "g":
            final_string = final_string + ascii_braille[char] 
        elif char == "h": 
            final_string = final_string + ascii_braille[char]
        elif char == "i":
            final_string = final_string + ascii_braille[char] 
        elif char == "j": 
            final_string = final_string + ascii_braille[char]
        elif char == "k": 
            final_string = final_string + ascii_braille[char]
        elif char == "l": 
            final_string = final_string + ascii_braille[char]
        elif char == "m": 
            final_string = final_string + ascii_braille[char]
        elif char == "n": 
            final_string = final_string + ascii_braille[char]
        elif char == "o":
            final_string = final_string + ascii_braille[char]
        elif char == "p": 
            final_string = final_string + ascii_braille[char]
        elif char == "q": 
            final_string = final_string + ascii_braille[char]
        elif char == "r": 
            final_string = final_string + ascii_braille[char]
        elif char == "s": 
            final_string = final_string + ascii_braille[char]
        elif char == "t": 
            final_string = final_string + ascii_braille[char]
        elif char == "u": 
            final_string = final_string + ascii_braille[char]
        elif char == "v": 
            final_string = final_string + ascii_braille[char]
        elif char == "w":
            final_string = final_string + ascii_braille[char] 
        elif char == "x": 
            final_string = final_string + ascii_braille[char]
        elif char == "y": 
            final_string = final_string + ascii_braille[char]
        elif char == "z":
            final_string = final_string + ascii_braille[char]
        elif char == " ":
            final_string = final_string + ascii_braille[char]
    return render_template('output.html', output=final_string)

@app.route('/convert-to-english', methods=['POST'])
def convert_to_english():

    english_dict = {
    '⠁': 'a', '⠃': 'b', '⠉': 'c', '⠙': 'd', '⠑': 'e',
    '⠋': 'f', '⠛': 'g', '⠓': 'h', '⠊': 'i', '⠚': 'j',
    '⠅': 'k', '⠇': 'l', '⠍': 'm', '⠝': 'n', '⠕': 'o',
    '⠏': 'p', '⠟': 'q', '⠗': 'r', '⠎': 's', '⠞': 't',
    '⠥': 'u', '⠧': 'v', '⠺': 'w', '⠭': 'x', '⠽': 'y', '⠵': 'z'
}

    # Get the input from home.html
    text_input = request.form['text']

    # Convert the text to braille
    english_text = ""
    for char in text_input.lower():
        if char in english_dict:
            english_text += english_dict[char]
        else:
            english_text += char

    return render_template('output.html', output=english_text)

if __name__ == "__main__":
    app.run()
