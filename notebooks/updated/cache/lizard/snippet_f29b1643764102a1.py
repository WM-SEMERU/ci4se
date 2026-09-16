def parse_mixed_delim_str(line):
    arrs = [[], [], []]
    for group in line.split(' '):
        for col, coord in enumerate(group.split('/')):
            if coord:
                arrs[col].append(int(coord))
    return [tuple(arr) for arr in arrs]