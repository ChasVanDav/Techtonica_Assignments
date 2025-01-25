# YouTube Video Details Scraper

A Flask-based web application to scrape, store, and display details of YouTube videos. This app uses the YouTube Data API to fetch video details such as title, description, publish date, channel name, and view count, and stores them in a PostgreSQL database.

## Features

- Extracts video details from YouTube URLs.
  ![Webpage Image](static/img/WebpageImage1.png)
- Stores the details in a PostgreSQL database.
  ![PostgresSQL Database](static/img/Postgresql%20Datavbase.png)
- Deletes video details from the database.
- Implements rate limiting to prevent abuse of the API.
- Requires Youtube Oauth 2 Authorization for security and anti-bot measures.
  ![API&Auth](static/img/YTOauth2&APIKey.png)
- Uses environment variables for secure configuration.
