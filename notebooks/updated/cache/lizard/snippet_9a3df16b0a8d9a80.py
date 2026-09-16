def _parse_reflectivity(line, lines):
    split_line = line.split()
    energy = float(split_line[0])
    reflect_xx = float(split_line[1])
    reflect_zz = float(split_line[2])
    return {'energy': energy, 'reflect_xx': reflect_xx, 'reflect_zz':
        reflect_zz}