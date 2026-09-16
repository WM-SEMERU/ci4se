def train(self):
    if not self.training_data:
        self.import_training_data()
    training_feature_set = [(self.extract_features(line), label) for line,
        label in self.training_data]
    self.classifier = nltk.NaiveBayesClassifier.train(training_feature_set)