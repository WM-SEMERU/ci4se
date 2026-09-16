def stopword_remove(self, items, threshold=False):

    def remove(tokens):
        return [t for t in tokens if t not in self.stopwords]
    if items == 'tokens':
        self.tokens = list(map(remove, self.tokens))
    elif items == 'stems':
        self.stems = list(map(remove, self.stems))
    else:
        raise ValueError("Items must be either 'tokens' or 'stems'.")