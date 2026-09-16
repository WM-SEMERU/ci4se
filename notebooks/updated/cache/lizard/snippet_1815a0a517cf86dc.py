def features(sentence, i):
    word = sentence[i]
    yield 'word:{}' + word.lower()
    if word[0].isupper():
        yield 'CAP'
    if i > 0:
        yield 'word-1:{}' + sentence[i - 1].lower()
        if i > 1:
            yield 'word-2:{}' + sentence[i - 2].lower()
    if i + 1 < len(sentence):
        yield 'word+1:{}' + sentence[i + 1].lower()
        if i + 2 < len(sentence):
            yield 'word+2:{}' + sentence[i + 2].lower()