def ngram_intersection(args, parser):
    store = utils.get_data_store(args)
    corpus = utils.get_corpus(args)
    catalogue = utils.get_catalogue(args)
    store.validate(corpus, catalogue)
    store.intersection(catalogue, sys.stdout)