def set_custom_boundary(doc):
    if doc.user_data == {}:
        raise AttributeError(
            'A list of Sentence is not attached to doc.user_data.')
    for token_nr, token in enumerate(doc):
        doc[token_nr].is_sent_start = False
    token_nr = 0
    for sentence in doc.user_data:
        doc[token_nr].is_sent_start = True
        token_nr += len(sentence.words)
    return doc