from scraper import Scraper

article = 'https://en.wikipedia.org/wiki/Shark'

scraper = Scraper(article)
links = scraper.get_links()

titles = [link for link in links.keys()]
print(titles)