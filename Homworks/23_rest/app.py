# Kishi "wawa" Wijaya
# SoftDev
# 11-20-24

import json
import urllib.request
from flask import Flask, render_template

app = Flask(__name__)
with open('key_nasa.txt', 'r') as file:
    DEMO_KEY = file.read()


with urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=' + DEMO_KEY) as response:
   info = response.read()




@app.route("/")
def main():
    return render_template("main.html", info = info)


if __name__ == "__main__":
    app.debug = True
    app.run()
