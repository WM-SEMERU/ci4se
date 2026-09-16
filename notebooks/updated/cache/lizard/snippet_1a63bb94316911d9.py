def _compute_relative_probs(self, prob_dict):
    for transition_counts in prob_dict.values():
        summed_occurences = sum(transition_counts.values())
        if summed_occurences > 0:
            for token in transition_counts.keys():
                transition_counts[token] = transition_counts[token
                    ] * 1.0 / summed_occurences