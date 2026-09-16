def _rec_filter_to_info(line):
    parts = line.rstrip().split('\t')
    move_filters = {'bSeq': 'strand', 'bPcr': 'damage'}
    new_filters = []
    bias_info = []
    for f in parts[6].split(';'):
        if f in move_filters:
            bias_info.append(move_filters[f])
        elif f not in ['.']:
            new_filters.append(f)
    if bias_info:
        parts[7] += ';DKFZBias=%s' % ','.join(bias_info)
    parts[6] = ';'.join(new_filters or ['PASS'])
    return '\t'.join(parts) + '\n'