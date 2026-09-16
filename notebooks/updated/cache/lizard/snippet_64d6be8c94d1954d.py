def fetchText(cls, url, data, textSearch, optional):
    if textSearch:
        match = textSearch.search(data[0])
        if match:
            text = match.group(1)
            out.debug('matched text %r with pattern %s' % (text, textSearch
                .pattern))
            return unescape(text).strip()
        if optional:
            return None
        else:
            raise ValueError('Pattern %s not found at URL %s.' % (
                textSearch.pattern, url))
    else:
        return None