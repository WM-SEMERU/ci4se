def tagify(suffix='', prefix='', base=SALT):
    parts = [base, TAGS.get(prefix, prefix)]
    if hasattr(suffix, 'append'):
        parts.extend(suffix)
    else:
        parts.append(suffix)
    for index, _ in enumerate(parts):
        try:
            parts[index] = salt.utils.stringutils.to_str(parts[index])
        except TypeError:
            parts[index] = str(parts[index])
    return TAGPARTER.join([part for part in parts if part])