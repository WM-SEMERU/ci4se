def clean_single_word(word, lemmatizing='wordnet'):
    if lemmatizing == 'porter':
        porter = PorterStemmer()
        lemma = porter.stem(word)
    elif lemmatizing == 'snowball':
        snowball = SnowballStemmer('english')
        lemma = snowball.stem(word)
    elif lemmatizing == 'wordnet':
        wordnet = WordNetLemmatizer()
        lemma = wordnet.lemmatize(word)
    else:
        print('Invalid lemmatizer argument.')
        raise RuntimeError
    return lemma