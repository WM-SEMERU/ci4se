def search(query, files, mode='sentence', regex=False):
    out = []
    sentences = convert_timestamps(files)
    if mode == 'fragment':
        out = fragment_search(query, sentences, regex)
    elif mode == 'word':
        out = word_search(query, sentences, regex)
    elif mode == 'franken':
        out = franken_sentence(query, files)
    else:
        out = sentence_search(query, sentences, regex)
    return out