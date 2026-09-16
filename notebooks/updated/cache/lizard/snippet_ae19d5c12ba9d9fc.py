def _parse_nodes_section(f, current_section, nodes):
    section = {}
    dimensions = None
    if current_section == 'NODE_COORD_SECTION':
        dimensions = 3
    elif current_section == 'DEMAND_SECTION':
        dimensions = 2
    else:
        raise ParseException('Invalid section {}'.format(current_section))
    n = 0
    for line in f:
        line = strip(line)
        definitions = re.split('\\s*', line)
        if len(definitions) != dimensions:
            raise ParseException(
                'Invalid dimensions from section {}. Expected: {}'.format(
                current_section, dimensions))
        node = int(definitions[0])
        values = [int(v) for v in definitions[1:]]
        if len(values) == 1:
            values = values[0]
        section[node] = values
        n = n + 1
        if n == nodes:
            break
    if n != nodes:
        raise ParseException('Missing {} nodes definition from section {}'.
            format(nodes - n, current_section))
    return section