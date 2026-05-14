documents = {
    'D1': 'the quick brown fox',
    'D2': 'the lazy dog sleeps',
    'D3': 'the fox jumps over the dog'
}
count = {}
def count_word(documnents):
    for sent in documents.values():
        words = sent.split(' ')
        for word in words:
            if word not in count:
                count[word] = 1
            else:
                count[word] += 1

count_word(documents)