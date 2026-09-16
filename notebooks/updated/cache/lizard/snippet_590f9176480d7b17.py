def urlencode2(query, doseq=0, safe='', querydelimiter='&'):
    if hasattr(query, 'items'):
        query = query.items()
    else:
        try:
            if len(query) and not isinstance(query[0], tuple):
                raise TypeError
        except TypeError:
            ty, va, tb = sys.exc_info()
            raise TypeError(
                'not a valid non-string sequence or mapping object ' + tb)
    l = []
    if not doseq:
        for k, v in query:
            k = quote_plus(str(k), safe=safe)
            v = quote_plus(str(v), safe=safe)
            l.append(k + '=' + v)
    else:
        for k, v in query:
            k = quote_plus(str(k), safe=safe)
            if isinstance(v, str):
                v = quote_plus(v, safe=safe)
                l.append(k + '=' + v)
            elif _is_unicode(v):
                v = quote_plus(v.encode('ASCII', 'replace'))
                l.append(k + '=' + v)
            else:
                try:
                    len(v)
                except TypeError:
                    v = quote_plus(str(v), safe=safe)
                    l.append(k + '=' + v)
                else:
                    for elt in v:
                        l.append(k + '=' + quote_plus(str(elt)))
    return querydelimiter.join(l)