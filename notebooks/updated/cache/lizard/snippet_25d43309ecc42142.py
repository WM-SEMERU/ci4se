def score(self, text):
    occurs = self.count_token_occurrences(self.tokenizer(text))
    scores = {}
    for category in self.categories.get_categories().keys():
        scores[category] = 0
    categories = self.categories.get_categories().items()
    for word, count in occurs.items():
        token_scores = {}
        for category, bayes_category in categories:
            token_scores[category] = float(bayes_category.get_token_count(word)
                )
        token_tally = sum(token_scores.values())
        if token_tally == 0.0:
            continue
        for category, token_score in token_scores.items():
            scores[category] += count * self.calculate_bayesian_probability(
                category, token_score, token_tally)
    final_scores = {}
    for category, score in scores.items():
        if score > 0:
            final_scores[category] = score
    return final_scores