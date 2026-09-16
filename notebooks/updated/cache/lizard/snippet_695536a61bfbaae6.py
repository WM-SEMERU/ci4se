def get_most_salient_words(vocab, topic_word_distrib, doc_topic_distrib,
    doc_lengths, n=None):
    return _words_by_salience_score(vocab, topic_word_distrib,
        doc_topic_distrib, doc_lengths, n)