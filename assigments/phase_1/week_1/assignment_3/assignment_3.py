def one_hot_encoding(sents):
    vocab = {}
    order = 0
    for sent in sents:
        for char in sent.split():
            if char not in vocab:
                vocab[char] = order
                order += 1
            else:
                continue
    
    print(vocab)
    list_vector = {}
    for i, word in enumerate(vocab):
        vector = [0 for _ in range(order)]
        vector[i] = 1
        list_vector[word] = vector
    return list_vector


sents = [
    "I love NLP",
    "NLP is fun"
]
print(one_hot_encoding(sents))