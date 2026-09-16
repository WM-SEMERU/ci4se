def from_command_line(command_line):
    assert is_iterable_typed(command_line, basestring)
    targets = []
    properties = []
    for e in command_line:
        if e[:1] != '-':
            if e.find('=') != -1 or looks_like_implicit_value(e.split('/')[0]):
                properties.append(e)
            elif e:
                targets.append(e)
    return [targets, properties]