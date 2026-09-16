def topic_search(text, corpus=doc_topic_vectors, pcaer=pcaer, corpus_text=
    corpus):
    tokens = tokenize(text, vocabulary=corpus.columns)
    tfidf_vector_query = np.array(tfidfer.transform([' '.join(tokens)]).
        todense())[0]
    topic_vector_query = pcaer.transform([tfidf_vector_query])
    query_series = pd.Series(topic_vector_query, index=corpus.columns)
    return corpus_text[query_series.dot(corpus.T).values.argmax()]