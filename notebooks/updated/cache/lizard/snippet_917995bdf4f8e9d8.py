def PositionedPhoneme(phoneme, word_initial=False, word_final=False,
    syllable_initial=False, syllable_final=False, env_start=False, env_end=
    False):
    pos_phoneme = deepcopy(phoneme)
    pos_phoneme.word_initial = word_initial
    pos_phoneme.word_final = word_final
    pos_phoneme.syllable_initial = syllable_initial
    pos_phoneme.syllable_final = syllable_final
    pos_phoneme.env_start = env_start
    pos_phoneme.env_end = env_end
    return pos_phoneme