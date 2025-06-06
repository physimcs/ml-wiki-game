from bs4 import BeautifulSoup
import requests

class Scraper:
    def __init__(self, current_link):
        self.parent_link = current_link
        self.child_links = []

    def get_links(self):
        response = requests.get(self.parent_link)
        soup = BeautifulSoup(response.text, 'html')

        main_content = soup.find(id='mw-content-text')
        links = main_content.find_all('a', href=True)

        internal_links = []
        for link in links:
            href = link['href']
            # Check to filter out non-internal links + unwanted internal links
            if href.startswith('/wiki') and ':' not in href and 'Wiki' not in href:
                url = 'https://en.wikipedia.org' + href
                internal_links.append(url)

        self.child_links = internal_links
        return self.child_links

stalin = Scraper('https://en.wikipedia.org/wiki/Joseph_Stalin')
all_links = stalin.get_links()
print(all_links)