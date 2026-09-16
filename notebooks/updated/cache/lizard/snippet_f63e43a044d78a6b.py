def _get_hangul_syllable_name(hangul_syllable):
    if not _is_hangul_syllable(hangul_syllable):
        raise ValueError(
            'Value passed in does not represent a Hangul syllable!')
    jamo = decompose_hangul_syllable(hangul_syllable, fully_decompose=True)
    result = ''
    for j in jamo:
        if j is not None:
            result += _get_jamo_short_name(j)
    return result