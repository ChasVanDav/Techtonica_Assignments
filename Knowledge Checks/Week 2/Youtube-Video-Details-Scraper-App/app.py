from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os
from models import db, VideoDetail
from youtube_videodetails import fetch_video_details, extract_video_id

# access .env file
load_dotenv()

# initialize app
app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')  # used for securely signing cookies

# getting database information
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('DB_USER')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# initialize database and migration tools (handles all SQL operations)
db.init_app(app)
migrate = Migrate(app, db)

# setting up rate limit variable for api calls, to avoid overloading and getting flagged by Youtube
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=[], # set the limit at function
)

# Route to start scraping video details from a YouTube video URL
@app.route('/start_scraping', methods=['POST'])
@limiter.limit("10 per minute")  # setting limit
def start_scraping():
    video_url = request.form.get('video_url')  
    video_id = extract_video_id(video_url)  

    if video_id:
        # Fetch video details using the video ID
        video_details = fetch_video_details(video_id)
    else:
        return "Error: Couldn't extract video ID."

    if video_details:
        # Save the video details to the database
        save_video_details_to_database(video_details)
        return redirect(url_for('index'))
    else:
        return "Error: Couldn't fetch video details." 

# Function to save video details to the database
def save_video_details_to_database(video_details):
    try:
        video_detail = VideoDetail(
            title=video_details['title'],
            description=video_details['description'],
            published_at=video_details['published_at'],
            channel_title=video_details['channel_title'],
            view_count=video_details['view_count']
        )
        # Add the video details to the database and save
        db.session.add(video_detail)
        db.session.commit()
        print(f"Saved video details: {video_details['title']}")
    except Exception as e:
        db.session.rollback()  # in case of an issue, rollback the transaction
        print(f"Error saving video details: {e}")

# Route to display video details on the homepage
@app.route('/')
def index():
    # Query the database for the 10 most recently published videos
    video_details = VideoDetail.query.order_by(VideoDetail.published_at.desc()).limit(10).all()
    # passing to index.html dynamically
    return render_template('index.html', video_details=video_details)

# Route to delete a video detail entry
@app.route('/delete_video/<int:video_id>', methods=['POST'])
def delete_video(video_id):
    # Find the video detail in the database by its ID
    video_detail = VideoDetail.query.get(video_id)
    if video_detail:
        # Delete the video detail from the database
        db.session.delete(video_detail)
        db.session.commit()
    return redirect(url_for('index')) 

# Rate limit exceeded handler
@app.errorhandler(429)
def ratelimit_handler(e):
    return f"Rate limit exceeded: {e.description}", 429 

# Main entry point to run the Flask app
if __name__ == '__main__':
    app.run(debug=True)  # Start the app in debug mode

