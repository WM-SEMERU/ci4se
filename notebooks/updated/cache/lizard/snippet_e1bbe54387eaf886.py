def get_pygments_style(style):
    if isinstance(style, StyleMeta):
        return style
    if '.' in style:
        module, name = style.rsplit('.', 1)
        return getattr(__import__(module, None, None, ['__name__']), name)
    elif style == 'sphinx':
        from sphinx.pygments_styles import SphinxStyle
        return SphinxStyle
    elif style == 'pyramid':
        from sphinx.pygments_styles import PyramidStyle
        return PyramidStyle
    elif style == 'none':
        from sphinx.pygments_styles import NoneStyle
        return NoneStyle
    else:
        return get_style_by_name(style)