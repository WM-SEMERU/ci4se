def _syllabify(word, T4=True):
    word = replace_umlauts(word)
    word, rules = apply_T1(word)
    if re.search('[^ieAyOauo]*([ieAyOauo]{2})[^ieAyOauo]*', word):
        word, T2 = apply_T2(word)
        word, T8 = apply_T8(word)
        word, T9 = apply_T9(word)
        word, T4 = apply_T4(word) if T4 else (word, '')
        rules += T2 + T8 + T9 + T4
    if re.search('[ieAyOauo]{3}', word):
        word, T6 = apply_T6(word)
        word, T5 = apply_T5(word)
        word, T7 = apply_T7(word)
        word, T2 = apply_T2(word)
        rules += T5 + T6 + T7 + T2
    word = replace_umlauts(word, put_back=True)
    rules = rules or ' T0'
    return word, rules