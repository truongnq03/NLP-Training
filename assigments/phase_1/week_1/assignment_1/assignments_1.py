import string
class Tokenize():
    def lowercase(self, text):
        lower = text.lower()
        return lower

    def normalize_whitespace(self, text):
        normalize = ' '.join(text.split())
        return normalize

    def tokenize_with_nopunctuation(self, text):
        for char in text:
            if char in string.punctuation:
                text = text.replace(char, "")      
        tokens = text.split()
        return tokens
    
    def pipeline(self, text):
        low = self.lowercase(text)
        print(low)
        nor = self.normalize_whitespace(low)
        print(nor)
        token = self.tokenize_with_nopunctuation(nor)
        print(token)

text = "HEllo,       WoRlD?"

tokenize = Tokenize()

tokenize.pipeline(text)