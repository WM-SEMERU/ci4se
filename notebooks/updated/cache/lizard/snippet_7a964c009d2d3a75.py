def apply_T8(word):
    WORD = word
    offset = 0
    for vv in tail_diphthongs(WORD):
        i = vv.start(1) + 1 + offset
        WORD = WORD[:i] + '.' + WORD[i:]
        offset += 1
    RULE = ' T8' if word != WORD else ''
    return WORD, RULE