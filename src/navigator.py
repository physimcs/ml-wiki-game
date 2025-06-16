from scraper import Scraper
from models import WikiModel

initial_url = "https://en.wikipedia.org/wiki/Glacial_landform"
scraper_instance = Scraper(initial_url)

links = scraper_instance.get_links()
target_title = "Peasant"

model = WikiModel(initial_url, target_title, links)
best_match = model.best_match()
print(best_match)