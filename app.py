#Import dependencies
## Use flask to render a template, redirect to another url, and create a URL
from flask import Flask, render_template, redirect, url_for
## Use PyMongo to interact with Mongo database
from flask_pymongo import PyMongo
##Convert from jupyter notebook to python when scraping
import scraping

#Set up flask
app = Flask(__name__)

#Tell Python how to connect to mongo using PyMongo
app.config["MONGO_URI"]="mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#Set up app routes

#Define the route for the HTML page
@app.route("/")
def index():
    mars=mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

#Define the route to scraping 
@app.route("/scrape")
def scrape ():
    mars = mongo.db.mars
    mars_data = scraping.scrape_all()
    mars.update_one({} {"$set":mars_data}, upsert = True)
    return redirect ('/', code=302)

#Tell Flask to run
if __name__ == "__main__":
    app.run()
