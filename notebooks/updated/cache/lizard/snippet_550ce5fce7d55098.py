def parse(cls, line, ns={}):
    definitions = []
    parses = [p for p in cls.compositor_spec.scanString(line)]
    if len(parses) != 1:
        raise SyntaxError('Invalid specification syntax.')
    else:
        e = parses[0][2]
        processed = line[:e]
        if processed.strip() != line.strip():
            raise SyntaxError('Failed to parse remainder of string: %r' %
                line[e:])
    opmap = {op.__name__: op for op in Compositor.operations}
    for group in cls.compositor_spec.parseString(line):
        if 'mode' not in group or group['mode'] not in ['data', 'display']:
            raise SyntaxError('Either data or display mode must be specified.')
        mode = group['mode']
        kwargs = {}
        operation = opmap[group['op']]
        spec = ' '.join(group['spec'].asList()[0])
        if group['op'] not in opmap:
            raise SyntaxError(
                'Operation %s not available for use with compositors.' %
                group['op'])
        if 'op_settings' in group:
            kwargs = cls.todict(group['op_settings'][0], 'brackets', ns=ns)
        definition = Compositor(str(spec), operation, str(group['value']),
            mode, **kwargs)
        definitions.append(definition)
    return definitions