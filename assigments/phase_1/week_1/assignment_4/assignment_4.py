def one_hot_encoding(sents, max_len=4):
    vocab = {}
    order = 0
    for sent in sents:
        for word in sent.split():
            if word not in vocab:
                vocab[word] = order
                order += 1
                
    print("Từ điển (Vocab):", vocab)
    vocab_size = len(vocab)
    
    padding_vector = [0 for _ in range(vocab_size)]
    
    encoded_sents = []
    
    for sent in sents:
        words = sent.split()
        
        if len(words) > max_len:
            words = words[:max_len]
            
        sent_vectors = []
        for word in words:
            word_idx = vocab[word]
            vector = [0 for _ in range(vocab_size)]
            vector[word_idx] = 1
            sent_vectors.append(vector)
            
        while len(sent_vectors) < max_len:
            sent_vectors.append(padding_vector)
            
        encoded_sents.append(sent_vectors)
        
    return encoded_sents

sents = [
    "I love NLP",    
    "NLP is fun",    
    "I love NLP and AI very much" 
]

result = one_hot_encoding(sents, max_len=4)

for idx, sent_matrix in enumerate(result):
    for vector in sent_matrix:
        print(vector)

    print("\n")
