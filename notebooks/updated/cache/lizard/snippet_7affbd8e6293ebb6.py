def url_norm(url, encoding=None):
    if isinstance(url, unicode):
        try:
            url = url.encode('ascii')
        except UnicodeEncodeError:
            pass
        encode_unicode = True
    else:
        encode_unicode = False
    urlparts = list(urlparse.urlsplit(url))
    urlparts[0] = urllib.unquote(urlparts[0]).lower()
    if urlparts[0] == 'mailto':
        url_fix_mailto_urlsplit(urlparts)
    is_idn = url_fix_host(urlparts)
    urlparts[3] = url_parse_query(urlparts[3], encoding=encoding)
    if urlparts[0] in urlparse.uses_relative:
        if not urlparts[2]:
            if urlparts[0] and (urlparts[3] or urlparts[4]):
                urlparts[2] = '/'
        else:
            urlparts[2] = collapse_segments(urlparts[2])
    urlparts[4] = urllib.unquote(urlparts[4])
    urlparts[0] = url_quote_part(urlparts[0], encoding=encoding)
    urlparts[1] = url_quote_part(urlparts[1], safechars='@:', encoding=encoding
        )
    urlparts[2] = url_quote_part(urlparts[2], safechars=_nopathquote_chars,
        encoding=encoding)
    urlparts[4] = url_quote_part(urlparts[4], encoding=encoding)
    res = urlunsplit(urlparts)
    if url.endswith('#') and not urlparts[4]:
        res += '#'
    if encode_unicode:
        res = unicode(res)
    return res, is_idn