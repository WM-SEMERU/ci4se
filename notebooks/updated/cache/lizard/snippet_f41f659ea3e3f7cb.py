def osf_crawl(k, *pths, **kw):
    from six.moves import reduce
    base = kw.pop('base', 'osfstorage')
    root = kw.pop('root', None)
    if len(kw) > 0:
        raise ValueError('Unknown optional parameters: %s' % (list(kw.keys()),)
            )
    if k.lower().startswith('osf:'):
        k = k[4:]
    k = k.lstrip('/')
    pths = [p.lstrip('/') for p in k.split('/') + list(pths)]
    bpth, pths = pths[0], pths[1:]
    if root is None:
        root = _osf_tree(bpth, base=base)
    return reduce(lambda m, k: m[k], pths, root)