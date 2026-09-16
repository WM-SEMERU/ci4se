def get_string(self, sigfigs=8):
    ctrl_dict = self.as_dict()
    lines = [] if 'HEADER' not in ctrl_dict else ['HEADER'.ljust(10) + self
        .header]
    if 'VERS' in ctrl_dict:
        lines.append('VERS'.ljust(10) + self.version)
    lines.append('STRUC'.ljust(10) + 'ALAT=' + str(round(ctrl_dict['ALAT'],
        sigfigs)))
    for l, latt in enumerate(ctrl_dict['PLAT']):
        if l == 0:
            line = 'PLAT='.rjust(15)
        else:
            line = ' '.ljust(15)
        line += ' '.join([str(round(v, sigfigs)) for v in latt])
        lines.append(line)
    for cat in ['CLASS', 'SITE']:
        for a, atoms in enumerate(ctrl_dict[cat]):
            if a == 0:
                line = [cat.ljust(9)]
            else:
                line = [' '.ljust(9)]
            for token, val in sorted(atoms.items()):
                if token == 'POS':
                    line.append('POS=' + ' '.join([str(round(p, sigfigs)) for
                        p in val]))
                else:
                    line.append(token + '=' + str(val))
            line = ' '.join(line)
            lines.append(line)
    return '\n'.join(lines) + '\n'