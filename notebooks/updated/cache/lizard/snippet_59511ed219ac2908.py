def style_from_pygments(style_cls=pygments_DefaultStyle, style_dict=None,
    include_defaults=True):
    assert style_dict is None or isinstance(style_dict, dict)
    assert style_cls is None or issubclass(style_cls, pygments_Style)
    styles_dict = {}
    if style_cls is not None:
        styles_dict.update(style_cls.styles)
    if style_dict is not None:
        styles_dict.update(style_dict)
    return style_from_dict(styles_dict, include_defaults=include_defaults)