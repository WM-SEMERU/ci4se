def create(fmt):
    w = None
    if fmt == 'tree':
        w = AsciiTreeGraphRenderer()
    elif fmt == 'dot':
        w = DotGraphRenderer(image_format='dot')
    elif fmt == 'png':
        w = DotGraphRenderer(image_format='png')
    elif fmt == 'ndot':
        w = NativeDotGraphRenderer()
    elif fmt == 'obo':
        w = OboFormatGraphRenderer()
    elif fmt == 'obog':
        w = OboJsonGraphRenderer()
    else:
        w = SimpleListGraphRenderer()
    return w