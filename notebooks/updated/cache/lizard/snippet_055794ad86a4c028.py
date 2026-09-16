def _all(field, value, document):
    try:
        a = set(value)
    except TypeError:
        raise MalformedQueryException("'$all' must accept an iterable")
    try:
        b = set(document.get(field, []))
    except TypeError:
        return False
    else:
        return a.intersection(b) == a