from flask import Flask, render_template, redirect, url_for
import os
from mars_image import full_image
from table import headings
from table import data
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", text="Latest Mars News", description="While Stargazing on Mars, NASA's Curiosity Rover Spots Earth and Venus", full_image=full_image, headings = headings, data=data)
if __name__ == "__main__":
    app.run(debug=True)