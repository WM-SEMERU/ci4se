def _convert_to_side(cls, side_spec):
    from openpyxl.styles import Side
    _side_key_map = {'border_style': 'style'}
    if isinstance(side_spec, str):
        return Side(style=side_spec)
    side_kwargs = {}
    for k, v in side_spec.items():
        if k in _side_key_map:
            k = _side_key_map[k]
        if k == 'color':
            v = cls._convert_to_color(v)
        side_kwargs[k] = v
    return Side(**side_kwargs)