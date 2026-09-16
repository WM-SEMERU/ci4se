def validate_cbarpos(value):
    patt = 'sh|sv|fl|fr|ft|fb|b|r'
    if value is True:
        value = {'b'}
    elif not value:
        value = set()
    elif isinstance(value, six.string_types):
        for s in re.finditer('[^%s]+' % patt, value):
            warn('Unknown colorbar position %s!' % s.group(), RuntimeWarning)
        value = set(re.findall(patt, value))
    else:
        value = validate_stringset(value)
        for s in (s for s in value if not re.match(patt, s)):
            warn('Unknown colorbar position %s!' % s)
            value.remove(s)
    return value