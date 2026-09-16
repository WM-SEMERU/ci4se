def _create_regex_pattern_add_optional_spaces_to_word_characters(word):
    r
    new_word = ''
    for ch in word:
        if ch.isspace():
            new_word += ch
        else:
            new_word += ch + '\\s*'
    return new_word