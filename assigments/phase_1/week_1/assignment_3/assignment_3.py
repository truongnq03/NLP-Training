def build_vocab(sents):
    vocab = {"<UNK>": 0}
    order = 1
    
    for sent in sents:
        for word in sent.split():
            if word not in vocab:
                vocab[word] = order
                order += 1
    return vocab

def one_hot_encoding(sents, vocab):
    vocab_size = len(vocab)
    all_sentences_encoded = []
    
    for sent in sents:
        words = sent.split()
        sent_vectors = []
        
        for word in words:
            word_index = vocab.get(word, vocab["<UNK>"])
            one_hot_vector = [0] * vocab_size
            one_hot_vector[word_index] = 1
            sent_vectors.append(one_hot_vector)
            
        all_sentences_encoded.append(sent_vectors)
        
    return all_sentences_encoded


train_sents = [
    "I love NLP",
    "NLP is fun"
]

vocab = build_vocab(train_sents)
print("Vocab:", vocab)

test_sents = [
    "I love NLP",
    "I love Deep Learning"
]

encoded_matrix = one_hot_encoding(test_sents, vocab)
print(encoded_matrix)