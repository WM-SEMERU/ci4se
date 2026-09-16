def get_sims(word, language, lemmatized=False, threshold=0.7):
    jv_replacer = JVReplacer()
    if language == 'latin':
        word = jv_replacer.replace(word).casefold()
    model_dirs = {'greek': '~/cltk_data/greek/model/greek_word2vec_cltk',
        'latin': '~/cltk_data/latin/model/latin_word2vec_cltk'}
    assert language in model_dirs.keys(
        ), 'Langauges available with Word2Vec model: {}'.format(model_dirs.
        keys())
    if lemmatized:
        lemma_str = '_lemmed'
    else:
        lemma_str = ''
    model_name = '{0}_s100_w30_min5_sg{1}.model'.format(language, lemma_str)
    model_dir_abs = os.path.expanduser(model_dirs[language])
    model_path = os.path.join(model_dir_abs, model_name)
    try:
        model = Word2Vec.load(model_path)
    except FileNotFoundError as fnf_error:
        print(fnf_error)
        print(
            "CLTK's Word2Vec models cannot be found. Please import '{}_word2vec_cltk'."
            .format(language))
        raise
    try:
        similars = model.most_similar(word)
    except KeyError as key_err:
        print(key_err)
        possible_matches = []
        for term in model.vocab:
            if term.startswith(word[:3]):
                possible_matches.append(term)
        print(
            "The following terms in the Word2Vec model you may be looking for: '{}'."
            .format(possible_matches))
        return None
    returned_sims = []
    for similar in similars:
        if similar[1] > threshold:
            returned_sims.append(similar[0])
    if not returned_sims:
        print(
            "Matches found, but below the threshold of 'threshold={}'. Lower it to see these results."
            .format(threshold))
    return returned_sims