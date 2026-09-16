def tfidf_corpus(docs=CORPUS):
    vectorizer = TfidfVectorizer()
    vectorizer = vectorizer.fit(docs)
    return vectorizer, vectorizer.transform(docs)