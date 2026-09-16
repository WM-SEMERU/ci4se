def reverse_word(word):
    op = get_letters(word)
    op.reverse()
    return ''.join(op)