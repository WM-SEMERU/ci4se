def get_url(width, height=None, background_color='cccccc', text_color=
    '969696', text=None, random_background_color=False):
    if random_background_color:
        background_color = _get_random_color()
    if not height:
        height = width
    d = dict(width=width, height=height, bcolor=background_color, tcolor=
        text_color)
    url = URL % d
    if text:
        text = text.replace(' ', '+')
        url = url + '?text=' + text
    return url