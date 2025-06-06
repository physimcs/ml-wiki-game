from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/Shark'
response = requests.get(url)
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

print(internal_links)