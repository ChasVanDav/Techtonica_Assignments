from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from models import db, VideoDetail
from youtube_videodetails import fetch_video_details, extract_video_id

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('DB_USER')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Route to home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to search for a video by title --> "Create HTML forms for user input" (READ)
@app.route('/search_video', methods=['GET'])
def search_video():
    search_query = request.args.get('query')
    if search_query:
        # Search for videos by title in the database
        video_details = VideoDetail.query.filter(VideoDetail.title.ilike(f"%{search_query}%")).all()
        return render_template('index.html', video_details=video_details, search_query=search_query)
    return redirect(url_for('index'))

# Route to scrape a video by URL (CREATE)
@app.route('/start_scraping', methods=['POST'])
def start_scraping():
    video_url = request.form.get('video_url')
    video_id = extract_video_id(video_url)
    
    if video_id:
        # Fetch video details from YouTube
        video_details = fetch_video_details(video_id)
        
        if video_details:
            # Save the video details in the database
            save_video_details_to_database(video_details)
            return redirect(url_for('index'))
        else:
            return "Error: Could not fetch video details."
    return "Error: Invalid YouTube URL."

# Function to save video details to the database --> "Store data in PostgreSQL database"
def save_video_details_to_database(video_details):
    video_detail = VideoDetail(
        title=video_details['title'],
        description=video_details['description'],
        published_at=video_details['published_at'],
        channel_title=video_details['channel_title'],
        view_count=video_details['view_count']
    )
    db.session.add(video_detail)
    db.session.commit()

# Route to delete a video (DELETE)
@app.route('/delete_video/<int:video_id>', methods=['POST'])
def delete_video(video_id):
    video_detail = VideoDetail.query.get(video_id)
    if video_detail:
        db.session.delete(video_detail)
        db.session.commit()
    return redirect(url_for('index'))

# Route to edit a video title --> "Develop Flask routes for CRUD operations" (UPDATE)
@app.route('/edit_video/<int:video_id>', methods=['GET', 'POST'])
def edit_video(video_id):
    video = VideoDetail.query.get(video_id)
    if request.method == 'POST':
        new_title = request.form['title']
        video.title = new_title
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_video.html', video=video)

if __name__ == '__main__':
    app.run(debug=True)

