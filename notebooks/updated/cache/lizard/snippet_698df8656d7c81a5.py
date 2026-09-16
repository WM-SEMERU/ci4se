def start_indexing(self):
    for filepath in self.filepaths:
        with open(filepath) as fp:
            blob = fp.read()
            self.words.extend(self.tokenize(blob))