def _get_format_callable(term, color, back_color):
    if isinstance(color, str):
        ensure(any(isinstance(back_color, t) for t in [str, type(None)]),
            TypeError, 'back_color must be a str or NoneType')
        if back_color:
            return getattr(term, '_'.join([color, 'on', back_color]))
        elif back_color is None:
            return getattr(term, color)
    elif isinstance(color, int):
        return term.on_color(color)
    else:
        raise TypeError('Invalid type {} for color'.format(type(color)))