from collections import Counter

class TermFrequency():
    def __init__(self):
        pass

    def compute(self, sents):
        all_tf_results = []

        for sent in sents:
            lower_words = sent.lower().split()
            total_term_in_sent = len(lower_words)
            
            counter = Counter(lower_words)
            
            sent_tf = {}
            for word in counter:
                sent_tf[word] = round(counter[word] / total_term_in_sent, 3)
            
            all_tf_results.append(sent_tf)

        return all_tf_results

documents = [
    "good boy",
    "good girl",
    "boy girl good"
]

tf = TermFrequency()
results = tf.compute(documents)

# In kết quả theo từng câu cho dễ nhìn
for idx, sent_tf in enumerate(results):
    print(f"Câu {idx + 1}: {documents[idx]}")
    print(f"-> TF: {sent_tf}\n")