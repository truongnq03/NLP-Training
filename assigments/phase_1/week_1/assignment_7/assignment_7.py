import re
import math

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
        print(sent_words_sets)
        idf_result = {}
        
        for word in self.vocab:
            df = sum(1 for word_set in sent_words_sets if word in word_set)
            
            idf_result[word] = math.log((N) / (df))
            
        return idf_result

documents = [
    "good boy",
    "good girl",
    "boy girl good"
]

idf = InverseDocumentFrequency()
# Khởi tạo từ điển trước
idf.create_list_vocab(documents)

# Tính toán IDF
idf_values = idf.compute(documents)

for word, val in idf_values.items():
    print(f"{word} {val:.4f}")