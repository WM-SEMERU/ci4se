def apply_T1(word):
    WORD = [w for w in re.split('([ieAyOauo]+)', word) if w]
    count = 0
    for i, v in enumerate(WORD):
        if i == 0 and is_consonant(v[0]):
            continue
        elif is_consonant(v[0]) and i + 1 != len(WORD):
            if is_cluster(v):
                if count % 2 == 0:
                    WORD[i] = v[0] + '.' + v[1:]
                else:
                    WORD[i] = '.' + v
            else:
                WORD[i] = v[:-1] + '.' + v[-1]
            count += 1
    WORD = ''.join(WORD)
    RULE = ' T1' if word != WORD else ''
    return WORD, RULE