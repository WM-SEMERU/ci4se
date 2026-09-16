def get_temporal_score_df(self):
    scoredf = {}
    tdf = self.term_ranker(self.corpus).get_ranks()
    for cat in sorted(self.corpus.get_categories()):
        if cat >= self.starting_time_step:
            negative_categories = self._get_negative_categories(cat, tdf)
            scores = self.term_scorer.get_scores(tdf[cat + ' freq'].astype(
                int), tdf[negative_categories].sum(axis=1))
            scoredf[cat + ' score'] = scores
            scoredf[cat + ' freq'] = tdf[cat + ' freq'].astype(int)
    return pd.DataFrame(scoredf)