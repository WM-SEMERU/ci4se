def parse_dirname(fc_dir):
    _, fc_dir = os.path.split(fc_dir)
    parts = fc_dir.split('_')
    name = None
    date = None
    for p in parts:
        if p.endswith(('XX', 'xx', 'XY', 'X2')):
            name = p
        elif len(p) == 6:
            try:
                int(p)
                date = p
            except ValueError:
                pass
    if name is None or date is None:
        raise ValueError('Did not find flowcell name: %s' % fc_dir)
    return name, date