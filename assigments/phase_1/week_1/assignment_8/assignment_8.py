import re
import math
from collections import Counter

class TermFrequency:
    def compute(self, sents):
        all_tf_results = []
        for sent in sents:
            lower_words = re.sub(r"[,!.?]", "", sent.lower()).split()
            total_term_in_sent = len(lower_words)
            counter = Counter(lower_words)
            
            sent_tf = {}
            for word in counter:
                sent_tf[word] = counter[word] / total_term_in_sent
            all_tf_results.append(sent_tf)
        return all_tf_results

class InverseDocumentFrequency:
    def __init__(self):
        self.vocab = {}

    def preprocess(self, sents):
        result = []
        for sent in sents:
            result.append(re.sub(r"[,!.?]", "", sent.lower()))
        return result

    def create_list_vocab(self, sents):
        order = 0
        for sent in self.preprocess(sents):
            for char in sent.split():
                if char not in self.vocab:
                    self.vocab[char] = order
                    order += 1
        return self.vocab

    def compute(self, sents):
        cleaned_sents = self.preprocess(sents)
        N = len(cleaned_sents)
        sent_words_sets = [set(sent.split()) for sent in cleaned_sents]
        
        idf_result = {}
        for word in self.vocab:
            df = sum(1 for word_set in sent_words_sets if word in word_set)
            
            # Sử dụng công thức toán tiêu chuẩn (N/df) như bạn mong muốn
            # Để tránh lỗi math domain error nếu df = 0, ta kiểm tra df > 0
            idf_result[word] = math.log(N / df) if df > 0 else 0.0
        return idf_result

class TFIDF:
    def __init__(self):
        self.tf_model = TermFrequency()
        self.idf_model = InverseDocumentFrequency()

    def fit_transform(self, sents):
        # 1. Khởi tạo từ điển và tính IDF
        vocab = self.idf_model.create_list_vocab(sents)
        idf_values = self.idf_model.compute(sents)
        
        # 2. Tính TF theo từng câu
        tf_values_per_sent = self.tf_model.compute(sents)
        
        # 3. Tạo Ma trận trống (List of Lists) bằng Python thuần
        # Kích thước: Số hàng = số câu, Số cột = số từ trong từ điển
        num_rows = len(sents)
        num_cols = len(vocab)
        matrix = [[0.0] * num_cols for _ in range(num_rows)]
        
        # 4. Điền giá trị TF-IDF vào đúng vị trí hàng và cột
        for row_idx, sent_tf in enumerate(tf_values_per_sent):
            for word, tf_val in sent_tf.items():
                if word in vocab:
                    col_idx = vocab[word] # Lấy vị trí cột
                    idf_val = idf_values.get(word, 0.0)
                    
                    # Điền vào ma trận dạng List 2 chiều
                    matrix[row_idx][col_idx] = round(tf_val * idf_val, 3)
            
        return matrix

documents = [
    "good boy",
    "good girl",
    "boy girl good"
]

tfidf_model = TFIDF()
matrix = tfidf_model.fit_transform(documents)

print(tfidf_model.idf_model.vocab)

print(matrix)