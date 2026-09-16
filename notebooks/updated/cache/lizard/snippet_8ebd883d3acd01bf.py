def parse_partlist(str):
    lines = str.strip().splitlines()
    lines = filter(len, lines)
    hind = header_index(lines)
    if hind is None:
        log.debug('empty partlist found')
        return [], []
    header_line = lines[hind]
    header = header_line.split('  ')
    header = filter(len, header)
    positions = [header_line.index(x) for x in header]
    header = [x.strip().split()[0].lower() for x in header]
    data_lines = lines[hind + 1:]

    def parse_data_line(line):
        y = [(h, line[pos1:pos2].strip()) for h, pos1, pos2 in zip(header,
            positions, positions[1:] + [1000])]
        return dict(y)
    data = [parse_data_line(x) for x in data_lines]
    return header, data