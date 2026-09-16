def tokenize(self):
    self.tokens = []
    self.terms = OrderedDict()
    for token in utils.tokenize(self.text):
        if token['unstemmed'] in self.stopwords:
            self.tokens.append(None)
        else:
            self.tokens.append(token)
            offsets = self.terms.setdefault(token['stemmed'], [])
            offsets.append(token['offset'])