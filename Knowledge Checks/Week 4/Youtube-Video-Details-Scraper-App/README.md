# 🍜 Korean Recipes & Top YT Videos

This is a Flask web application that scrapes recipe titles from a CNN article and displays YouTube video details based on recipe titles. Users can view the embedded YouTube video and details such as title, views, channel name, and publish date.

## 🚀 Tech Stack

- **Backend:** Flask, Flask-SQLAlchemy
- **Database:** PostgreSQL
- **API Integration:** YouTube Data API v3
- **Other:** Python-dotenv for environment variables

## 📂 Project Structure

```
YouTube-Video-Details-Scraper-App/
│-- app.py                  # Main application file
│-- database.py             # Database connection setup
│-- models.py               # Database models
│-- webscraper.py           # Web scraping utility
│-- init_db.py              # Initialize the database
│-- requirements.txt        # Dependencies
│-- .env                    # Environment variables (excluded from repo)
|-- .gitignore              # Specifies files and directories to be excluded from version control
│-- static/
│   ├── css/
│   │   ├── styles.css      # Styling for the app
│-- templates/
│   ├── index.html          # Homepage template
│   ├── video.html          # Video details page
│   ├── edit_video.html     # Edit video title page
```

## 🛠️ Setup Instructions

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/yourusername/YouTube-Video-Details-Scraper-App.git
cd YouTube-Video-Details-Scraper-App
```

### 2️⃣ Create a Virtual Environment & Install Dependencies

```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Set Up Environment Variables

Create a `.env` file in the root directory and add:

```
YOUTUBE_API_KEY=your_youtube_api_key_here
DATABASE_URL=postgresql://your_username@localhost/your_database_name
```

### 4️⃣ Initialize the Database

Run the `init_db.py` script to initialize the database:

```sh
python init_db.py
```

This will create the necessary tables in your PostgreSQL database.

### 5️⃣ Run the Application

```sh
flask run
```

Access the app at: `http://127.0.0.1:5000/`

## 🤝 Contributing

1. 🍴 Fork the repository
2. 🌱 Create a new branch (`git checkout -b feature-branch`)
3. 💾 Commit your changes (`git commit -m "Added new feature"`)
4. 🚀 Push to the branch (`git push origin feature-branch`)
5. 🔥 Open a Pull Request

## 📜 License

This project is licensed under the MIT License.
