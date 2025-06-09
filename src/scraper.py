from bs4 import BeautifulSoup
import requests

class Scraper:
    """
    Scraper that extracts internal links from a Wikipedia article.
    """
    def __init__(self, url):
        """
        Initializes scraper.

        Args: 
        url (str): Full url of article
        """
        self.parent_link = url
        self.child_links = {}

    def scrape_links(self):
        response = requests.get(self.parent_link)
        soup = BeautifulSoup(response.text, 'lxml')

        main_content = soup.find(id='mw-content-text')
        links = main_content.find_all('a', href=True)

        return links
    
    def get_links(self):
        links = self.scrape_links()

        internal_links = {}
        for link in links:
            href = link['href']
            # Check to filter out non-internal links + unwanted internal links
            if href.startswith('/wiki') and ':' not in href and 'Wiki' not in href:
                url = 'https://en.wikipedia.org' + href
                title = href[6::].replace('_', ' ')
                internal_links[title] = url

        self.child_links = internal_links
        return self.child_links