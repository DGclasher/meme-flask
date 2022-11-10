import os
from flask import Flask, render_template
import requests
import json

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
	meme_pic, subreddit = get_meme()
	return render_template("index.html", meme_pic=meme_pic, subreddit=subreddit)

# if __name__ == "main":
    # port  = int(os.environ.get("PORT", 3000))
app.run(debug=False, port=5000)
