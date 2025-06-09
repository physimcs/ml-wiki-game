from scraper import Scraper

initial_url = 'https://en.wikipedia.org/wiki/Shark'
scraper_instance = Scraper(initial_url)
links = scraper_instance.get_links()

print(links)
