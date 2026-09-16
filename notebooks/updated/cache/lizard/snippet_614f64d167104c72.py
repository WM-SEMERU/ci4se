def _foursquare_urlencode(query, doseq=0, safe_chars='&/,+'):
    if hasattr(query, 'items'):
        query = query.items()
    else:
        try:
            if len(query) and not isinstance(query[0], tuple):
                raise TypeError
        except TypeError:
            ty, va, tb = sys.exc_info()
            raise TypeError('not a valid non-string sequence or mapping object'
                ).with_traceback(tb)
    l = []
    if not doseq:
        for k, v in query:
            k = parse.quote(_as_utf8(k), safe=safe_chars)
            v = parse.quote(_as_utf8(v), safe=safe_chars)
            l.append(k + '=' + v)
    else:
        for k, v in query:
            k = parse.quote(_as_utf8(k), safe=safe_chars)
            if isinstance(v, six.string_types):
                v = parse.quote(_as_utf8(v), safe=safe_chars)
                l.append(k + '=' + v)
            else:
                try:
                    len(v)
                except TypeError:
                    v = parse.quote(_as_utf8(v), safe=safe_chars)
                    l.append(k + '=' + v)
                else:
                    for elt in v:
                        l.append(k + '=' + parse.quote(_as_utf8(elt)))
    return '&'.join(l)