import json
import re
import copy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from tabulate import tabulate

class Search:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(
            ngram_range=(1, 2),
            max_features=None
        )
        self.tfidf_matrix = None
        self.original_products = []
    
    def load(self):
        with open("assigments\\phase_1\\week_1\\assignment_10\\products.json", "r", encoding="utf-8") as f:
            list_product = json.load(f)
        return list_product
    
    def preprocess(self, list_product):
        processed_list = copy.deepcopy(list_product)
        for product in processed_list:
            product_name = product["product_name"]
            clear_space = " ".join(product_name.split())
            short_name = re.split(r"-", clear_space)[0].strip()
            lower = short_name.lower()
            product["clean_name_for_search"] = lower
        return processed_list
    
    def prepare_search_engine(self, list_product):
        self.original_products = list_product
        processed_list = self.preprocess(list_product)
        corpus = [product["clean_name_for_search"] for product in processed_list]
        self.tfidf_matrix = self.vectorizer.fit_transform(corpus)
    
    def search(self, user_input, top_n=3):
        user_input_clean = user_input.lower()
        query_vectorize = self.vectorizer.transform([user_input_clean])
        cosine_scores = cosine_similarity(query_vectorize, self.tfidf_matrix).flatten()
        top_indices = cosine_scores.argsort()[::-1][:top_n]
        
        results = []
        for idx in top_indices:
            if cosine_scores[idx] > 0:
                matched_product = self.original_products[idx].copy()
                matched_product["cosine_score"] = round(float(cosine_scores[idx]), 4)
                results.append(matched_product)
                
        return results

search_engine = Search()
raw_data = search_engine.load()
search_engine.prepare_search_engine(raw_data)
user_query = input("Nhap san pham can tim: ")
search_results = search_engine.search(user_query, top_n=10)

table_data = []
for idx, item in enumerate(search_results, start=1):
    table_data.append([
        idx,
        item["product_name"],
        item["current_price"],
        item["original_price"] if item["original_price"] else "N/A",
        item["discount"] if item["discount"] else "0%",
        f"{item['cosine_score']:.4f}"
    ])

headers = ["STT", "Tên Sản Phẩm", "Giá Hiện Tại", "Giá Gốc", "Giảm Giá", "Điểm Cosine"]

print(tabulate(table_data, headers=headers, tablefmt="fancy_grid", maxcolwidths=[None, 40, None, None, None, None]))