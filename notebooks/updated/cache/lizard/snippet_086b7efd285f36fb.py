def get_sentence_break_property(value, is_bytes=False):
    obj = (unidata.ascii_sentence_break if is_bytes else unidata.
        unicode_sentence_break)
    if value.startswith('^'):
        negated = value[1:]
        value = '^' + unidata.unicode_alias['sentencebreak'].get(negated,
            negated)
    else:
        value = unidata.unicode_alias['sentencebreak'].get(value, value)
    return obj[value]