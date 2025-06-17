from scraper import Scraper
from models import WikiModel
import wikipedia

initial = wikipedia.search(input('Enter your initial article title: '))[0]
target_title = input('Enter your target article title: ')

initial_url = 'https://en.wikipedia.org/wiki/' + initial.replace(' ', '_')

def navigate(current_article, target_title):
    print(f"Currently at: {current_article}")

    if current_article == 'https://en.wikipedia.org/wiki/' + target_title.replace(' ', '_'):
        return "Game won!"

    scraper = Scraper(current_article)
    links = scraper.get_links()

    model = WikiModel(initial_url, target_title, links)
    best_match = model.best_match()

    return navigate(best_match[1], target_title)

match = navigate(initial_url, target_title)
print(match)