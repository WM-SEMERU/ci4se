def use_neutral_categories(self):
    term_df = self.term_ranker.get_ranks()
    self.priors += term_df[[(c + ' freq') for c in self.
        _get_neutral_categories()]].sum(axis=1)
    return self