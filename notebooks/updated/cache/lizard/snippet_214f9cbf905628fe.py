def rouge_l_sentence_level(evaluated_sentences, reference_sentences):
    if len(evaluated_sentences) <= 0 or len(reference_sentences) <= 0:
        raise ValueError('Collections must contain at least 1 sentence.')
    reference_words = _split_into_words(reference_sentences)
    evaluated_words = _split_into_words(evaluated_sentences)
    m = len(reference_words)
    n = len(evaluated_words)
    lcs = _len_lcs(evaluated_words, reference_words)
    return _f_lcs(lcs, m, n)