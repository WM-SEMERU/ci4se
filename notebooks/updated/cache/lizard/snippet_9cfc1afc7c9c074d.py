def parse_mouse_allele_name(name):
    original = name
    if name.upper().startswith('H2'):
        name = name[2:]
    elif name.upper().startswith('H-2'):
        name = name[3:]
    _, name = parse_separator(name)
    if name.upper().startswith('I'):
        if len(name) < 2:
            raise AlleleParseError('Incomplete mouse MHC allele: %s' % original
                )
        gene_name = name[:2]
        name = name[2:]
    else:
        if len(name) < 1:
            raise AlleleParseError('Incomplete mouse MHC allele: %s' % original
                )
        gene_name = name[0]
        name = name[1:]
    _, name = parse_separator(name)
    if len(name) != 1:
        raise AlleleParseError(
            'Malformed mouse MHC allele: %s, parse error at %s' % (original,
            name))
    allele = name[0]
    return gene_name.upper(), allele.lower()