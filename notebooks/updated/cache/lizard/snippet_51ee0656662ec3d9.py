def get_color_mode(mode):
    name = mode.upper()
    name = name.rstrip('A')
    name = {'1': 'BITMAP', 'L': 'GRAYSCALE'}.get(name, name)
    return getattr(ColorMode, name)