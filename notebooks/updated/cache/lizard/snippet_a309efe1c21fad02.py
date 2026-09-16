def any_to_rgb(color):
    if isinstance(color, tuple):
        if len(color) == 3:
            color = color + (255,)
        return color
    if isinstance(color, str):
        return parse_color(color)
    raise ValueError('Color not recognized: {}'.format(color))