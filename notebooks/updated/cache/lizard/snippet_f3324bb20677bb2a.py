def get_name_dictionary_extractor(name_trie):
    return DictionaryExtractor().set_trie(name_trie).set_pre_filter(
        VALID_TOKEN_RE.match).set_pre_process(lambda x: x.lower()
        ).set_metadata({'extractor': 'dig_name_dictionary_extractor'})