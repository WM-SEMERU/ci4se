def is_retroflex(c, lang):
    o = get_offset(c, lang)
    return o >= RETROFLEX_RANGE[0] and o <= RETROFLEX_RANGE[1]