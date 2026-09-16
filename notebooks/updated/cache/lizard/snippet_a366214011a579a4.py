def token_perplexity_micro(eval_data, predictions, scores, learner='ignored'):
    lens = np.array([(len(_maybe_tokenize(inst.output)) + 1) for inst in
        eval_data])
    return [np.exp(np.average(-np.array(scores) / lens, weights=lens))]