from flask import Flask, render_template

from giphy_api import get_gifs
from graphiql_request import get_profiles

app = Flask(__name__)

@app.route("/")
def index():
    giphy_res = get_gifs()
    return render_template("index.html", gifs=giphy_res, enumerate=enumerate)

@app.route("/about")
def about():
    profiles = get_profiles()
    return render_template("about.html", members=profiles, enumerate=enumerate)

app.run(debug=True)
