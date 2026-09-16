def prune_overridden(ansi_string):
    multi_seqs = set(p for p in RE_ANSI.findall(ansi_string) if ';' in p[1])
    for escape, codes in multi_seqs:
        r_codes = list(reversed(codes.split(';')))
        try:
            r_codes = r_codes[:r_codes.index('0') + 1]
        except ValueError:
            pass
        for group in CODE_GROUPS:
            for pos in reversed([i for i, n in enumerate(r_codes) if n in
                group][1:]):
                r_codes.pop(pos)
        reduced_codes = ';'.join(sorted(r_codes, key=int))
        if codes != reduced_codes:
            ansi_string = ansi_string.replace(escape, '\x1b[' +
                reduced_codes + 'm')
    return ansi_string