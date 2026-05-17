import re

class BagOfWord:
    def __init__(self):
        self.vocab = {}

    def preprocess(self, sents):
        result = []

        for sent in sents:
            result.append(re.sub(r"[,!,.?]", "", sent))
        return result

    def create_list_vocab(self, sents):
        order = 0
        for sent in self.preprocess(sents):
            for char in sent.split():
                if char not in self.vocab:
                    self.vocab[char] = order
                    order += 1
                else:
                    continue
        return self.vocab
    
    def vectorize(self, sents):
        raise NotImplementedError("Chưa cài đặt ở hàm con")
    
class CountBagOfWord(BagOfWord):
    def vectorize(self, sents):
        preproc = self.preprocess(sents)
        vocab = self.create_list_vocab(preproc)
        result = []
        for sent in preproc:
            vector = [0 for _ in range(len(vocab))]
            for word in sent.split():
                index = vocab[word]
                vector[index] += 1
            result.append(vector)
        
        return result
        
class BinaryBagOfWord(BagOfWord):
    def vectorize(self, sents):
        preproc = self.preprocess(sents)
        vocab = self.create_list_vocab(preproc)
        result = []
        for sent in preproc:
            vector = [0 for _ in range(len(vocab))]
            for word in sent.split():
                index = vocab[word]
                vector[index] = 1
            result.append(vector)
        
        return result

documents = [
    "NLP, is fun?",
    "I love NLP love.",
    "NLP NLP NLP is love me!"
]

cbow = CountBagOfWord()
bbow = BinaryBagOfWord()

print("Count BagOfWord: ", cbow.vectorize(documents))
print("Binary BagOfWord: ", bbow.vectorize(documents))