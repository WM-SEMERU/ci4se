def get_shape(torch_node):
    m = re.match('.*Float\\(([\\d\\s\\,]+)\\).*', str(next(torch_node.
        outputs())))
    if m:
        shape = m.group(1)
        shape = shape.split(',')
        shape = tuple(map(int, shape))
    else:
        shape = None
    return shape