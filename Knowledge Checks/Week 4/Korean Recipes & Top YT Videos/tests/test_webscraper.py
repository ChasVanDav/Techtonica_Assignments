# This tests the webscraper "get_subheaders" function to ensure that it properly extracta text

import unittest
from webscraper import get_subheaders
import requests_mock

class TestWebScraper(unittest.TestCase):
    
    def test_get_subheaders(self):
        # URL for the CNN page
        url = 'https://www.cnn.com/travel/article/best-korean-dishes/index.html'
        
        # mock the HTML content returned from the web
        mock_html = """
        <html>
            <body>
                <h2 class="subheader inline-placeholder">Bibimbap</h2>
                <h2 class="subheader inline-placeholder">Kimchi</h2>
                <h2 class="subheader inline-placeholder">Bulgogi</h2>
            </body>
        </html>
        """
        
        # mock the HTTP GET request
        with requests_mock.Mocker() as mock:
            mock.get(url, text=mock_html)
            
            # call the get_subheaders function
            subheaders = get_subheaders()
            print("Subheaders:", subheaders)
            
            # verify the returned subheaders are correct
            self.assertEqual(subheaders, ['Bibimbap', 'Kimchi', 'Bulgogi'])

if __name__ == '__main__':
    unittest.main()
