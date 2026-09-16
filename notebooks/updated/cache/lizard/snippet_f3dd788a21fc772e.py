def f2p_word(word, max_word_size=15, cutoff=3):
    original_word = word
    word = word.lower()
    c = dictionary.get(word)
    if c:
        return [(c, 1.0)]
    if word == '':
        return []
    elif len(word) > max_word_size:
        return [(original_word, 1.0)]
    results = []
    for w in variations(word):
        results.extend(f2p_word_internal(w, original_word))
    results.sort(key=lambda r: r[1], reverse=True)
    return results[:cutoff]