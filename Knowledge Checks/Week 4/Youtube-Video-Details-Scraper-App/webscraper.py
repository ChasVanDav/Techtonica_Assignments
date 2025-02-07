import requests
from bs4 import BeautifulSoup

def get_subheaders():
    # URL of the website to scrape
    url = 'https://www.cnn.com/travel/article/best-korean-dishes/index.html'
    
    # Fetch the webpage
    page = requests.get(url)
    
    # Parse the HTML content
    soup = BeautifulSoup(page.text, 'html.parser')

    # Find all the subheader elements by their unique class
    subheaders = soup.find_all(class_="subheader inline-placeholder")

    # Extract text from each subheader
    subheader_texts = [subheader.get_text(strip=True) for subheader in subheaders]

    return subheader_texts
