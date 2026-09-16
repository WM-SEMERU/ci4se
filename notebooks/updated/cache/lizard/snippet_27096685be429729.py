def nltk_tokenize_words(string, attached_period=False, language=None):
    assert isinstance(string, str), 'Incoming string must be type str.'
    if language == 'sanskrit':
        periods = ['.', '।', '॥']
    else:
        periods = ['.']
    punkt = PunktLanguageVars()
    tokens = punkt.word_tokenize(string)
    if attached_period:
        return tokens
    new_tokens = []
    for word in tokens:
        for char in periods:
            if word.endswith(char):
                new_tokens.append(word[:-1])
                new_tokens.append(char)
                break
        else:
            new_tokens.append(word)
    return new_tokens