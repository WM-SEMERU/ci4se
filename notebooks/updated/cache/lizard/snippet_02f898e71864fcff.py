def create(technical_terms_filename, spellchecker_cache_path):
    user_dictionary = os.path.join(os.getcwd(), 'DICTIONARY')
    user_words = read_dictionary_file(user_dictionary)
    technical_terms_set = set(user_words)
    if technical_terms_filename:
        with open(technical_terms_filename) as tech_tf:
            technical_terms_set |= set(tech_tf.read().splitlines())
    return Dictionary(technical_terms_set, 'technical_words',
        dictionary_sources=[technical_terms_filename, user_dictionary],
        cache=spellchecker_cache_path)