def check_section(node, section, keys=None):
    if keys:
        for key in keys:
            if key not in node:
                raise ValueError('Missing key %r inside %r node' % (key,
                    section))