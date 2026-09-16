def collect(context=None, style=None, palette=None, **kwargs):
    params = {}
    if context:
        params.update(get(context, 'context', **kwargs))
    if style:
        params.update(get(style, 'style', **kwargs))
    if palette:
        params.update(get(palette, 'palette', **kwargs))
    return params