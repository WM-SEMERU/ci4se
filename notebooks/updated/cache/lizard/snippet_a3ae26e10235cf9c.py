def spell(word):
    w = Word(word)
    candidates = common([word]) or exact([word]) or known([word]) or known(w
        .typos()) or common(w.double_typos()) or [word]
    correction = max(candidates, key=NLP_COUNTS.get)
    return get_case(word, correction)