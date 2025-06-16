from scraper import Scraper
import torch
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

initial_url = 'https://en.wikipedia.org/wiki/Feudal'
scraper_instance = Scraper(initial_url)
links = scraper_instance.get_links()

target_title = "Peasant"
article_titles = list(links.keys())

corpus_embeddings = model.encode(article_titles, convert_to_tensor=True)
corpus_embeddings = util.normalize_embeddings(corpus_embeddings)

query_embedding = model.encode([target_title], convert_to_tensor=True)
query_embedding = util.normalize_embeddings(query_embedding)

hits = util.semantic_search(query_embedding, corpus_embeddings, top_k=1, score_function=util.dot_score)
top_match = hits[0][0]

best_title = article_titles[top_match["corpus_id"]]
best_link = links[best_title]