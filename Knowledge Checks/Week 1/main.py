from flask import Flask, render_template # connect to dynamically display on html
import requests # htttp requests to get info from the web
from bs4 import BeautifulSoup # for webscraping
from flask_sqlalchemy import SQLAlchemy # store and display data

# create instance of app
app = Flask(__name__)

# Flask default database set up
# configure local (///) database file set up in the working directory via sqlite engine
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subheaders.db'
# we don't need to track changes for this simple app
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# initialize SQLAlchemy for this app
db = SQLAlchemy(app)

# creating a database table aka "Model" called 'Subheader'
class Subheader(db.Model):
    # column 1 = autogenerate unique id number(integer)
    id = db.Column(db.Integer, primary_key=True)
    # column 2 = text(string) up to 200 characters per object, cannot be empty
    text = db.Column(db.String(200), nullable=False)

    # function to display the relevant data for each object in this class
    # in this case, we dont need to see the id, and display only the text
    def __repr__(self):
        return f'<Subheader {self.text}>'

# function to webscrape an article that has a list of 39 Korean dishes
# There are "subheaders" or titles and "paragraphs" or content, for this app,
# we will only scrape the titles.
def get_subheaders():
    # URL of the website
    url = 'https://www.cnn.com/travel/article/best-korean-dishes/index.html'
    # Fetch the webpage
    page = requests.get(url)
    # Parse the HTML content and assign to 'soup'
    soup = BeautifulSoup(page.text, 'html.parser')

    # this is the unique class for the titles of Korean dishes
    subheaders = soup.find_all(class_="subheader inline-placeholder")

    # Extract text from each subheader
    subheader_texts = [subheader.get_text(strip=True) for subheader in subheaders]

    return subheader_texts

# Set up a route for the homepage aka the only page on this app
@app.route("/")
def home():
    # Calling back to the Subheader class on line 18 and 
    # checking if there are any objects
    existing_subheaders = Subheader.query.all()

    if not existing_subheaders:  # If no subheaders exist, scrape and store them
        # First, get the subheaders by scraping
        subheaders = get_subheaders()

        # Store each subheader in the database
        for subheader_text in subheaders:
            new_subheader = Subheader(text=subheader_text)
            db.session.add(new_subheader)

        # Commit the changes to the database
        db.session.commit()

    # Fetch all subheaders from the database to display
    stored_subheaders = Subheader.query.all()

    return render_template("index.html", subheaders=stored_subheaders)

# Run the app
if __name__ == '__main__':
    # Create the database tables (if they don't exist yet)
    with app.app_context():
        db.create_all()

    app.run(debug=True)
