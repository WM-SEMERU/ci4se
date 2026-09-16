def apply_u_umlaut(stem: str):
    assert len(stem) > 0
    s_stem = s.syllabify_ssp(stem.lower())
    if len(s_stem) == 1:
        last_syllable = OldNorseSyllable(s_stem[-1], VOWELS, CONSONANTS)
        last_syllable.apply_u_umlaut()
        return ''.join(s_stem[:-1]) + str(last_syllable)
    else:
        penultimate_syllable = OldNorseSyllable(s_stem[-2], VOWELS, CONSONANTS)
        last_syllable = OldNorseSyllable(s_stem[-1], VOWELS, CONSONANTS)
        penultimate_syllable.apply_u_umlaut()
        last_syllable.apply_u_umlaut(True)
        last_syllable.apply_u_umlaut(True)
        return ''.join(s_stem[:-2]) + str(penultimate_syllable) + str(
            last_syllable)