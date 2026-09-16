def is_arabicword(word):
    if len(word) == 0:
        return False
    elif re.search('([^\u0600-ْ%s%s%s])' % (LAM_ALEF, LAM_ALEF_HAMZA_ABOVE,
        LAM_ALEF_MADDA_ABOVE), word):
        return False
    elif is_haraka(word[0]) or word[0] in (WAW_HAMZA, YEH_HAMZA):
        return False
    elif re.match('^(.)*[%s](.)+$' % ALEF_MAKSURA, word):
        return False
    elif re.match('^(.)*[%s]([^%s%s%s])(.)+$' % (TEH_MARBUTA, DAMMA, KASRA,
        FATHA), word):
        return False
    else:
        return True