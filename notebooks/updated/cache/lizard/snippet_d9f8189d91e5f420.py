def correct_word(word_string):
    if word_string is None:
        return ''
    elif isinstance(word_string, str):
        return max(find_candidates(word_string), key=find_word_prob)
    else:
        raise InputError(
            'string or none type variable not passed as argument to correct_word'
            )