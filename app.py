# Dependencies 
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create instance of Flask app 
app = Flask(__name__)

# Connect to MongoDB 
app.config["MONGO_URI"] = 'mongodb://localhost:27017/mars'
mongo = PyMongo(app)
# app.config['MONGO_CONNECT'] = False

# Home route
@app.route("/")
def home():
    # Find data in MongoDB (within connection)
    mars_info = mongo.db.mars.find_one()

    # Render HTML template 
    return render_template("index.html", mars_info=mars_info)

# Scrape route


# Run the application
if __name__ == "__main__":
    app.run(debug=True)