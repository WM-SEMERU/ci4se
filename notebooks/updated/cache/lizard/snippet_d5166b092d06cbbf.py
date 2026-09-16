def _parse_ipa_syllable(unparsed_syllable):
    ipa_tone = re.search('[%(marks)s]+' % {'marks': _IPA_MARKS},
        unparsed_syllable)
    if not ipa_tone:
        syllable, tone = unparsed_syllable, '5'
    else:
        for tone_number, tone_mark in _IPA_TONES.items():
            if ipa_tone.group() == tone_mark:
                tone = tone_number
                break
        syllable = unparsed_syllable[0:ipa_tone.start()]
    return syllable, tone