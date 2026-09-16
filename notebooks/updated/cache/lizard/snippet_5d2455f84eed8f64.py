def get_most_relevant_words_for_topic(vocab, rel_mat, topic, n=None):
    _check_relevant_words_for_topic_args(vocab, rel_mat, topic)
    return _words_by_score(vocab, rel_mat[topic], least_to_most=False, n=n)