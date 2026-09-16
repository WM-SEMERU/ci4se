def _parse_disambiguate(disambiguatestatsfilename):
    disambig_stats = [0, 0, 0]
    with open(disambiguatestatsfilename, 'r') as in_handle:
        for i, line in enumerate(in_handle):
            fields = line.strip().split('\t')
            if i == 0:
                assert fields == ['sample', 'unique species A pairs',
                    'unique species B pairs', 'ambiguous pairs']
            else:
                disambig_stats = [(x + int(y)) for x, y in zip(
                    disambig_stats, fields[1:])]
    return disambig_stats