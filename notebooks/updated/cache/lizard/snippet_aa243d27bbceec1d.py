def train(self, *args, **kwargs):
    self.classifier = self.nltk_class.train(self.positive_features, self.
        unlabeled_features, self.positive_prob_prior)
    return self.classifier