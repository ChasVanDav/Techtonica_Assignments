<!-- # YouTube Video Details Scraper

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
- Uses environment variables for secure configuration. -->

## Knowledge Check - Week 3

Requirements:

- **Create HTML forms for user input (search queries, article selection)**
- **Implement client-side form validation**
- Develop Flask routes for CRUD operations (create, read, **update**, delete)
- Store data in PostgreSQL database

### Key Updates

- Added search feature that filters saved list of scraped videos by title
- Added edit button (and route) to edit video title
- Added client-side form validation for incorrect input if Youtube url does not match expectation as defined.

### Search results for "a"

![Search results for 'a'](static/img/searchresultwitha.png)

### Search results for "daaimah"

![Search results for 'daaimah'](static/img/searchresultwithdaaimah.png)

### Client-side Input Validation for Youtube URL

![Input validation for Youtube URL](static/img/userinputvalidation.png)

### Editing Video Title

![editing Video title](static/img/edittitle.png)

### Updated Video Title

![Saved edited Video title](static/img/savededittitle.png)
