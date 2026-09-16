def extract_text(fpath):
    with codecs.open(fpath, 'r') as f:
        document = f.read()
    encoding = chardet.detect(document)['encoding']
    document = document.decode(encoding)
    tokens = []
    sentences = []
    i = 0
    for sentence in nltk.tokenize.sent_tokenize(document):
        sentences.append(i)
        for word in nltk.tokenize.word_tokenize(sentence):
            tokens.append(word)
            i += 1
    contexts = [('sentence', sentences)]
    return StructuredFeature(tokens, contexts)