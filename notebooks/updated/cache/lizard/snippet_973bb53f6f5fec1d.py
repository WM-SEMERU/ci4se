def _pop_colors_and_alpha(glyphclass, kwargs, prefix='', default_alpha=1.0):
    result = dict()
    color = kwargs.pop(prefix + 'color', get_default_color())
    for argname in ('fill_color', 'line_color'):
        if argname not in glyphclass.properties():
            continue
        result[argname] = kwargs.pop(prefix + argname, color)
    if 'text_color' in glyphclass.properties():
        result['text_color'] = kwargs.pop(prefix + 'text_color', 'black')
    alpha = kwargs.pop(prefix + 'alpha', default_alpha)
    for argname in ('fill_alpha', 'line_alpha', 'text_alpha'):
        if argname not in glyphclass.properties():
            continue
        result[argname] = kwargs.pop(prefix + argname, alpha)
    return result