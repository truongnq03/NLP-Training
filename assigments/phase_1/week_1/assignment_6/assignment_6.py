from collections import Counter

class TermFrequency():
    def __init__(self):
        pass

    def compute(self, sents):
        all_tf_results = []
        vocab = set()

        for sent in sents:
            lower_words = sent.lower().split()
            total_term_in_sent = len(lower_words)
            
            counter = Counter(lower_words)
            vocab.update(lower_words)
            
            sent_tf = {}
            for word in counter:
                sent_tf[word] = round(counter[word] / total_term_in_sent, 3)
            
            all_tf_results.append(sent_tf)

        sorted_vocab = sorted(list(vocab))

        tf_array = []
        for sent_tf in all_tf_results:
            row = [sent_tf.get(word, 0.0) for word in sorted_vocab]
            tf_array.append(row)

        return tf_array, sorted_vocab

documents = [
    "good boy",
    "good girl",
    "boy girl good"
]

tf = TermFrequency()
tf_matrix, vocabulary = tf.compute(documents)

print("Vocabulary (Thứ tự các cột):", vocabulary)
print("TF Array:")
for row in tf_matrix:
    print(row)
