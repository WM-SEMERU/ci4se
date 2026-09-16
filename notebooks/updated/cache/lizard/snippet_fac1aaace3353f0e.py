def get_random_ontology(TOP_RANGE=10, pattern=''):
    choices = get_localontologies(pattern=pattern)
    try:
        ontouri = choices[random.randint(0, TOP_RANGE)]
    except:
        ontouri = choices[0]
    print('Testing with URI: %s' % ontouri)
    g = get_pickled_ontology(ontouri)
    if not g:
        g = do_pickle_ontology(ontouri)
    return ontouri, g