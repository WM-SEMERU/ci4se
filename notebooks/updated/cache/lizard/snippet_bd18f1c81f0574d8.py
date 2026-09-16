def score_cosine(self, term1, term2, **kwargs):
    t1_kde = self.kde(term1, **kwargs)
    t2_kde = self.kde(term2, **kwargs)
    return 1 - distance.cosine(t1_kde, t2_kde)