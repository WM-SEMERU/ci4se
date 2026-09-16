def format_word_list_mixedcase(word_list):
    to_return, first_word = list(), True
    for word in word_list:
        if first_word:
            to_return.append(word.lower())
            first_word = False
        else:
            to_return.append(word.capitalize())
    return to_return