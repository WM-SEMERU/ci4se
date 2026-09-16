def get_word_break_property(value, is_bytes=False):
    obj = unidata.ascii_word_break if is_bytes else unidata.unicode_word_break
    if value.startswith('^'):
        negated = value[1:]
        value = '^' + unidata.unicode_alias['wordbreak'].get(negated, negated)
    else:
        value = unidata.unicode_alias['wordbreak'].get(value, value)
    return obj[value]