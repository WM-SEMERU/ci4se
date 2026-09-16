def build_headermap(headers):
    headermap = {}
    for hfile in headers:
        headermap[hfile] = None
    for hfile in headers:
        assert hfile.startswith('c/') or hfile.startswith('datatable/include/')
        inc = find_includes(hfile)
        for f in inc:
            assert f != hfile, 'File %s includes itself?' % f
            assert f.startswith('c/')
            if f not in headers:
                raise ValueError('Unknown header "%s" included from %s' % (
                    f, hfile))
        headermap[hfile] = set(inc)
    return headermap