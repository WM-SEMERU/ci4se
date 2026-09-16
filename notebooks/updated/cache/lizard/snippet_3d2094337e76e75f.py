def get_indic_positional_category_property(value, is_bytes=False):
    if PY35:
        obj = (unidata.ascii_indic_positional_category if is_bytes else
            unidata.unicode_indic_positional_category)
        alias_key = 'indicpositionalcategory'
    else:
        obj = (unidata.ascii_indic_matra_category if is_bytes else unidata.
            unicode_indic_matra_category)
        alias_key = 'indicmatracategory'
    if value.startswith('^'):
        negated = value[1:]
        value = '^' + unidata.unicode_alias[alias_key].get(negated, negated)
    else:
        value = unidata.unicode_alias[alias_key].get(value, value)
    return obj[value]