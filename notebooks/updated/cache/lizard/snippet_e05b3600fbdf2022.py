def from_file(filename):
    spec = Spec()
    with open(filename, 'r', encoding='utf-8') as f:
        parse_context = {'current_subpackage': None}
        for line in f:
            spec, parse_context = _parse(spec, parse_context, line)
    return spec