def get_feature_penalty(self):
    if self.feature_penalty is None:
        self.feature_penalty = self.get_field('feature_penalty')
    return self.feature_penalty