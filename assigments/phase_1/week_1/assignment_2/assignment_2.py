import re

class VietNameseTextProcessor:
    def sentence_tokenize(self, text):
        return re.split(r"(?<=[.!?])\s+|\n+", text)

    def word_tokenize(self, text):
        result = []
        for sent in text:
            result.append(sent.split())
        flat = [x for xs in result for x in xs]
        return flat

    def remove_urls(self, text):
        return re.sub(r"https?://\S+|www\.\S+", "", text)

    def remove_html(self, text):
        return re.sub(r"<[^>]+>", "", text)

    def remove_emojis(self, text):
        return re.sub(r"[\U00010000-\U0010ffff]|\u2600-\u27bf", "", text)

    def remove_punctuation(self, text):
        result = []
        for sent in text:
            result.append(re.sub(r"[!,.?]", "", sent))
        return result

    def normalize_whitespace(self, text):
        result = []
        for sent in text:
            result.append(' '.join(sent.split()))

        return result

    def remove_stopwords(self, text):
        with open("assigments\\phase_1\\week_1\\assignment_2\\stopword.txt", encoding="utf-8") as f:
            stopword = f.read()
            stop_arr = set(stopword.split())
        result = [word.lower() for word in text if word.lower() not in stop_arr]
        return result


    def preprocess(self, text):
        url = self.remove_urls(text)
        html = self.remove_html(url)
        emoji = self.remove_emojis(html)
        sent_tokenize = self.sentence_tokenize(emoji)
        nor_whitespace = self.normalize_whitespace(sent_tokenize)
        puct = self.remove_punctuation(nor_whitespace)
        word_tokenize = self.word_tokenize(puct)
        stopword = self.remove_stopwords(word_tokenize)
        return stopword

text = """<p>Xin chào!!!</p>
        Tôi đang học lập trình NLP 😄
        Vào TRang này https://abc.com !!! Chào ông Mr.X"""

processor = VietNameseTextProcessor()

print(processor.preprocess(text))


    