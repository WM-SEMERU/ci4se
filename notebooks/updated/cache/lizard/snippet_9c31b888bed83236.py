def load(self, lemmatizer_path):
    self.lemmatizer = {}
    with io.open(lemmatizer_path, encoding='utf-8') as data_file:
        raw = json.load(data_file)
        for entry in raw:
            self.lemmatizer[entry['Form']] = entry['Lemmas']
    self.apply_blacklist()