import os
import logging
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy.orm import Session
import requests
from webscraper import get_subheaders
from models import Recipe 
from database import SessionLocal, engine


# Load environment variables from .env file
load_dotenv()

# Get YouTube API Key from environment variables
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

# Flask app setup
app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

def search_youtube(query):
    try:
        # Make an API call to search for the video
        youtube_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&key={YOUTUBE_API_KEY}&maxResults=5"
        response = requests.get(youtube_url)
        video_data = response.json()

        # Log the response for debugging purposes
        logging.debug("Response from YouTube API: %s", video_data)

        # print("Response from YouTube API:", video_data)

        # Loop through items until a youtube#video is found
        for video in video_data.get('items', []):
            # Check if the result is a video (not a channel)
            if video.get('id', {}).get('kind') == 'youtube#video':
                video_id = video['id'].get('videoId', None)
                if video_id:  # Ensure video_id exists
                    video_url = f"https://www.youtube.com/watch?v={video_id}"
                    video_title = video['snippet']['title']
                    channel_title = video['snippet']['channelTitle']
                    published_at = video['snippet']['publishedAt']

                    # Now fetch the video statistics (e.g., view count)
                    stats_url = f"https://www.googleapis.com/youtube/v3/videos?part=statistics&id={video_id}&key={YOUTUBE_API_KEY}"
                    stats_response = requests.get(stats_url)
                    stats_data = stats_response.json()

                    view_count = None
                    if 'items' in stats_data:
                        view_count = stats_data['items'][0]['statistics'].get('viewCount', 0)

                    # Create metadata to store in the database
                    video_metadata = {
                        'channelTitle': channel_title,
                        'publishedAt': published_at,
                        'viewCount': view_count
                    }

                    return video_id, video_url, video_title, video_metadata

    except requests.RequestException as e:
        logging.error("Error making YouTube API request: %s", e)
        # If no video found, return None
        return None, None, None, None


def clean_subheader(title):
    """
    Clean the subheader text by removing unwanted characters like quotes, parentheses, etc.
    Modify this function as needed to handle specific cleaning rules.
    """
    cleaned_title = title.replace('“', '').replace('”', '')  # Removing quotes
    cleaned_title = cleaned_title.replace('(', '').replace(')', '')  # Removing parentheses
    cleaned_title = cleaned_title.strip()  # Remove leading and trailing whitespace
    return cleaned_title

@app.route('/')
def home():
    logging.debug('Home page is loading...')

    session = SessionLocal()

    # Fetch all subheaders from your database
    subheaders = session.query(Recipe.recipe_title).all()

    # Clean the subheaders before rendering
    cleaned_subheaders = [clean_subheader(title[0]) for title in subheaders]

    # If no subheaders are found, run the web scraper and insert into the DB
    if not subheaders:
        try:
            subheader_texts = get_subheaders()  # Call the web scraper function
            
            if not subheader_texts:  # Check if empty list is returned
                raise ValueError("No data returned from web scraper.")

            # Clean and store in the database
            cleaned_subheader_texts = [clean_subheader(title) for title in subheader_texts]
            for title in cleaned_subheader_texts:
                recipe = Recipe(recipe_title=title)
                session.add(recipe)

            session.commit()
            session.close()
            return render_template('index.html', subheaders=cleaned_subheader_texts)

        except Exception as e:
            logging.error(f"Web scraping failed: Incorrect URL or website issue. Error: {e}")
            session.close()
            return render_template('500.html', error_message="Sorry, we couldn't fetch the recipes. Please try again later.")

    # Close the session after fetching the data
    session.close()
    return render_template('index.html', subheaders=cleaned_subheaders)

@app.route('/video/<string:title>', methods=['GET'])
def get_video(title):
    # Open a session to interact with the database
    with SessionLocal() as session:
        # Search for the title in the database
        recipe = session.query(Recipe).filter(Recipe.recipe_title == title).first()

        # If the recipe exists, search YouTube for its video
        if recipe:
            video_id, video_url, video_title, video_metadata = search_youtube(title)

            # Format the view count with commas
            if video_metadata and video_metadata.get('viewCount'):
                view_count = int(video_metadata['viewCount'])
                formatted_view_count = "{:,}".format(view_count)
                video_metadata['viewCount'] = formatted_view_count

            # Update the database with the video details
            if video_id:
                recipe.video_id = video_id
                recipe.video_url = video_url
                recipe.video_title = video_title
                recipe.video_metadata = video_metadata

                session.commit()

            return render_template('video.html', recipe=recipe, video_id=video_id, video_metadata=video_metadata)
        
        # If no recipe found, return 404
        return render_template('404.html'), 404


@app.route('/edit_video/<int:video_id>', methods=['GET', 'POST'])
def edit_video(video_id):
    # Create a session to interact with the database
    with SessionLocal() as session:
        # Retrieve the video by its ID
        video = session.query(Recipe).filter(Recipe.id == video_id).first()

        if not video:
            return "Video not found", 404
        
        if request.method == 'POST':
            # Get the new title from the form
            new_title = request.form['title']
            
            # Update the video title in the database
            video.recipe_title = new_title
            session.commit()

            # Redirect to the list of videos after the update
            return redirect(url_for('home'))

        # If GET request, show the form with the current title
        return render_template('edit_video.html', video=video)

# Custom error pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500

@app.errorhandler(Exception)
def handle_exception(e):
    return render_template('error.html'), 500


if __name__ == '__main__':
    app.run(debug=True)



