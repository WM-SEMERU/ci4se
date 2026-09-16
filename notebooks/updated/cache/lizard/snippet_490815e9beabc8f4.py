def _normalize_tags(chunk):
    ret = []
    for word, tag in chunk:
        if tag == 'NP-TL' or tag == 'NP':
            ret.append((word, 'NNP'))
            continue
        if tag.endswith('-TL'):
            ret.append((word, tag[:-3]))
            continue
        if tag.endswith('S'):
            ret.append((word, tag[:-1]))
            continue
        ret.append((word, tag))
    return ret