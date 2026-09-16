def update(self, new_data, *args, **kwargs):
    self.train_set += new_data
    self.train_features = [(self.extract_features(d), c) for d, c in self.
        train_set]
    try:
        self.classifier = self.nltk_class.train(self.train_features, *args,
            **kwargs)
    except AttributeError:
        raise ValueError(
            'NLTKClassifier must have a nltk_class variable that is not None.')
    return True