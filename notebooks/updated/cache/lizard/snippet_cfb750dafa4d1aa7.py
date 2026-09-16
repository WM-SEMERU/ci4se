def parse_name_string(full_name):
    name = Name()
    if ',' in full_name:
        toks = full_name.split(',')
        name.family = toks[0]
        name.given = ','.join(toks[1:]).strip()
    else:
        toks = full_name.split()
        name.given = toks[0]
        name.family = ' '.join(toks[1:]).strip()
    return name