from sentence_transformers import SentenceTransformer, util
from scraper import Scraper

class WikiModel:
    def __init__(self, current_link, target_link, internal_link_pairs):
        self.current_link = current_link
        self.target_link = target_link
        self.article_titles = list(internal_link_pairs.keys())
        self.articles = internal_link_pairs
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
    
    def best_match(self):
        corpus_embeddings = self.model.encode(
            self.article_titles, convert_to_tensor=True
        )
        corpus_embeddings = util.normalize_embeddings(corpus_embeddings)

        query_embedding = self.model.encode(
            [self.target_link], convert_to_tensor=True
        )
        query_embedding = util.normalize_embeddings(query_embedding)

        hits = util.semantic_search(
            query_embedding, corpus_embeddings, top_k=5, score_function=util.dot_score
        )

        top_matches = hits[0]
        results = []
        for match in top_matches:
            article = self.article_titles[match['corpus_id']]
            results.append(article)
        return tuple(results)


initial_url = "https://en.wikipedia.org/wiki/Glacial_landform"
target_title = "Peasant"

scraper = Scraper(initial_url)
links = scraper.get_links()

model = WikiModel(initial_url, target_title, links)
best_match = model.best_match()

print(best_match)