def _from_frame_string(contents):
    lines = contents.split('\n')
    num_sites = int(lines[0])
    coords = []
    sp = []
    coord_patt = re.compile(
        '(\\w+)\\s+([0-9\\-\\+\\.eEdD]+)\\s+([0-9\\-\\+\\.eEdD]+)\\s+([0-9\\-\\+\\.eEdD]+)'
        )
    for i in range(2, 2 + num_sites):
        m = coord_patt.search(lines[i])
        if m:
            sp.append(m.group(1))
            xyz = [val.lower().replace('d', 'e') for val in m.groups()[1:4]]
            coords.append([float(val) for val in xyz])
    return Molecule(sp, coords)