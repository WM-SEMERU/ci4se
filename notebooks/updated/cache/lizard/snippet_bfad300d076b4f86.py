def slugify(text, delim='-'):
    result = []
    for word in _punct_re.split((text or '').lower()):
        result.extend(codecs.encode(word, 'ascii', 'replace').split())
    return delim.join([str(r) for r in result])