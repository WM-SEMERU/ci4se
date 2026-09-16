def Prefix(docs, drop=0.0):
    ids = numpy.zeros((sum(len(doc) for doc in docs),), dtype='i')
    i = 0
    for doc in docs:
        for token in doc:
            ids[i] = token.prefix
            i += 1
    return ids, None