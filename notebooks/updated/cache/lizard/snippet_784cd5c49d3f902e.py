def gather_positions(tree):
    pos = {'data-x': 'r0', 'data-y': 'r0', 'data-z': 'r0', 'data-rotate-x':
        'r0', 'data-rotate-y': 'r0', 'data-rotate-z': 'r0', 'data-scale':
        'r0', 'is_path': False}
    steps = 0
    default_movement = True
    for step in tree.findall('step'):
        steps += 1
        for key in POSITION_ATTRIBS:
            value = step.get(key)
            if value is not None:
                default_movement = False
                pos[key] = value
            elif pos[key] and not pos[key].startswith('r'):
                pos[key] = 'r0'
        if steps == 1 and pos['data-scale'] == 'r0':
            pos['data-scale'] = '1'
        if default_movement and steps != 1:
            pos['data-x'] = 'r%s' % DEFAULT_MOVEMENT
        if 'data-rotate' in step.attrib:
            pos['data-rotate-z'] = step.get('data-rotate')
            del step.attrib['data-rotate']
        if 'hovercraft-path' in step.attrib:
            default_movement = False
            pos['is_path'] = True
            pos['path'] = step.attrib['hovercraft-path']
            yield pos.copy()
            del pos['path']
        else:
            if 'data-x' in step.attrib or 'data-y' in step.attrib:
                pos['is_path'] = False
            yield pos.copy()