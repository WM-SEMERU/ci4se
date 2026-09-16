def _collapse_language_array(language_array):
    language_dict = {}
    for language in language_array.item:
        key = language.key[0]
        value = language.value[0]
        language_dict[key] = value
    return language_dict