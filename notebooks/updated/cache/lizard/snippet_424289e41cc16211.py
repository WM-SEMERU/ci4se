def from_file(filename='feff.inp'):
    with zopen(filename, 'rt') as f:
        lines = list(clean_lines(f.readlines()))
    params = {}
    eels_params = []
    ieels = -1
    ieels_max = -1
    for i, line in enumerate(lines):
        m = re.match('([A-Z]+\\d*\\d*)\\s*(.*)', line)
        if m:
            key = m.group(1).strip()
            val = m.group(2).strip()
            val = Tags.proc_val(key, val)
            if key not in ('ATOMS', 'POTENTIALS', 'END', 'TITLE'):
                if key in ['ELNES', 'EXELFS']:
                    ieels = i
                    ieels_max = ieels + 5
                else:
                    params[key] = val
        if ieels >= 0:
            if i >= ieels and i <= ieels_max:
                if i == ieels + 1:
                    if int(line.split()[1]) == 1:
                        ieels_max -= 1
                eels_params.append(line)
    if eels_params:
        if len(eels_params) == 6:
            eels_keys = ['BEAM_ENERGY', 'BEAM_DIRECTION', 'ANGLES', 'MESH',
                'POSITION']
        else:
            eels_keys = ['BEAM_ENERGY', 'ANGLES', 'MESH', 'POSITION']
        eels_dict = {'ENERGY': Tags._stringify_val(eels_params[0].split()[1:])}
        for k, v in zip(eels_keys, eels_params[1:]):
            eels_dict[k] = str(v)
        params[str(eels_params[0].split()[0])] = eels_dict
    return Tags(params)