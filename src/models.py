from sentence_transformers import SentenceTransformer, util

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
            query_embedding, corpus_embeddings, top_k=1, score_function=util.dot_score
        )
        top_match = hits[0][0]

        best_title = self.article_titles[top_match["corpus_id"]]
        best_link = self.articles[best_title]

        return [best_title, best_link]