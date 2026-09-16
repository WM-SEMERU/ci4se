def version(i):
    o = i.get('out', '')
    r = get_version({})
    if r['return'] > 0:
        return r
    version_str = r['version_str']
    if o == 'con':
        out('V' + version_str)
    return r