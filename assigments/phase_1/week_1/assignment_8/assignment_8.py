import re
import math
from collections import Counter

class TermFrequency:
    def compute(self, cleaned_sents):
        all_tf_results = []
        for sent_words in cleaned_sents:
            total_term_in_sent = len(sent_words)
            counter = Counter(sent_words)
            
            sent_tf = {}
            for word in counter:
                sent_tf[word] = counter[word] / total_term_in_sent
            all_tf_results.append(sent_tf)
        return all_tf_results

class InverseDocumentFrequency:
    def compute(self, cleaned_sents, vocab):
        N = len(cleaned_sents)
        sent_words_sets = [set(sent) for sent in cleaned_sents]
        
        idf_result = {}
        for word in vocab:
            df = sum(1 for word_set in sent_words_sets if word in word_set)
            idf_result[word] = math.log((N + 1) / (df + 1)) + 1
        return idf_result

class TFIDF:
    def __init__(self):
        self.tf_model = TermFrequency()
        self.idf_model = InverseDocumentFrequency()
        self.vocab = {}

    def _preprocess(self, sents):
        cleaned_sents = []
        for sent in sents:
            words = re.sub(r"[,!.?]", "", sent.lower()).split()
            cleaned_sents.append(words)
        return cleaned_sents

    def _create_vocab(self, cleaned_sents):
        order = 0
        for sent_words in cleaned_sents:
            for word in sent_words:
                if word not in self.vocab:
                    self.vocab[word] = order
                    order += 1
        return self.vocab

    def fit_transform(self, sents):
        cleaned_sents = self._preprocess(sents)
        vocab = self._create_vocab(cleaned_sents)
        
        idf_values = self.idf_model.compute(cleaned_sents, vocab)
        tf_values_per_sent = self.tf_model.compute(cleaned_sents)

        print(tf_values_per_sent)
        
        num_rows = len(sents)
        num_cols = len(vocab)
        matrix = [[0.0] * num_cols for _ in range(num_rows)]
        
        for row_idx, sent_tf in enumerate(tf_values_per_sent):
            for word, tf_val in sent_tf.items():
                if word in vocab:
                    col_idx = vocab[word]
                    idf_val = idf_values.get(word, 0.0)
                    matrix[row_idx][col_idx] = round(tf_val * idf_val, 3)

        for row_idx in range(num_rows):
            row_sum_squares = sum(val ** 2 for val in matrix[row_idx])
            if row_sum_squares > 0:
                l2_norm = math.sqrt(row_sum_squares)
                for col_idx in range(num_cols):
                    matrix[row_idx][col_idx] = round(matrix[row_idx][col_idx] / l2_norm, 3)
            
        return matrix

documents = [
    "good boy",
    "good girl",
    "boy girl good"
]

tfidf_model = TFIDF()
matrix = tfidf_model.fit_transform(documents)

print(tfidf_model.vocab)
print(matrix)