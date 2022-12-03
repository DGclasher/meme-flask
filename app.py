import os
from flask import Flask, render_template
import requests
import json
from datetime import datetime

app = Flask(__name__)
app.static_folder = 'static'


def get_meme():
    url = "https://meme-api.herokuapp.com/gimme"
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large, subreddit


@app.route('/')
def index():
    year_now = datetime.utcnow().year
    meme_pic, subreddit = get_meme()
    return render_template("index.html", meme_pic=meme_pic, year=year_now, subreddit=subreddit)


if __name__ == "main":
    the_port  = int(os.environ.get("PORT", 3000))
    app.run(port=the_port ,debug=False)
