from scraper import Scraper
from models import WikiModel

initial_url = "https://en.wikipedia.org/wiki/Glacial_landform"
target_title = "Peasant"

def navigate(current_article, target_title):
    print(f"Currently at: {current_article}")

    if current_article == 'https://en.wikipedia.org/wiki/' + target_title:
        return "Game won!"

    scraper = Scraper(current_article)
    links = scraper.get_links()

    model = WikiModel(initial_url, target_title, links)
    best_match = model.best_match()

    return navigate(best_match[1], target_title)

result = navigate(initial_url, target_title)
print(result)