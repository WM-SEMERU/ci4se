def report_ucs_msg(ucs, wcwidth_libc, wcwidth_local):
    ucp = ucs.encode('unicode_escape')[2:].decode('ascii').upper().lstrip('0')
    url = 'http://codepoints.net/U+{}'.format(ucp)
    name = unicodedata.name(ucs)
    return 'libc,ours={},{} [--o{}o--] name={} val={} {} '.format(wcwidth_libc,
        wcwidth_local, ucs, name, ord(ucs), url)