def _make_canonical_headers(headers, headers_to_sign):
    pairs = []
    for name in headers_to_sign:
        if name not in headers:
            continue
        values = headers[name]
        if not isinstance(values, (list, tuple)):
            values = [values]
        comma_values = b','.join(' '.join(line.strip().split()) for value in
            values for line in value.splitlines())
        pairs.append((name.lower(), comma_values))
    sorted_pairs = sorted(b'%s:%s' % (name, value) for name, value in
        sorted(pairs))
    return b'\n'.join(sorted_pairs) + b'\n'