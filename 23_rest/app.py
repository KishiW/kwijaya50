# Kishi "wawa" Wijaya
# SoftDev
# 11-20-24

import json
import urllib.request
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'wawa'




@app.route("/")
def main():
    data = urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=56fF6PjUPBIHJZmL00z4LXc6oTakAu7y0hRihvht')
    jsonDictionary = json.loads(data.read().decode())
    photo = jsonDictionary["url"]
    return render_template('main.html', photo = photo, info = jsonDictionary["explanation"])


if __name__ == "__main__":
    app.debug = True
    app.run()
