def joinMeiUyir(mei_char, uyir_char):
    if not mei_char:
        return uyir_char
    if not uyir_char:
        return mei_char
    if not isinstance(mei_char, PYTHON3 and str or unicode):
        raise ValueError(
            "Passed input mei character '%s' must be unicode, not just string"
             % mei_char)
    if not isinstance(uyir_char, PYTHON3 and str or unicode
        ) and uyir_char != None:
        raise ValueError(
            "Passed input uyir character '%s' must be unicode, not just string"
             % uyir_char)
    if mei_char not in grantha_mei_letters:
        raise ValueError(
            "Passed input character '%s' is not a tamil mei character" %
            mei_char)
    if uyir_char not in uyir_letters:
        raise ValueError(
            "Passed input character '%s' is not a tamil uyir character" %
            uyir_char)
    if uyir_char:
        uyiridx = uyir_letters.index(uyir_char)
    else:
        return mei_char
    meiidx = grantha_mei_letters.index(mei_char)
    uyirmeiidx = meiidx * 12 + uyiridx
    return grantha_uyirmei_letters[uyirmeiidx]