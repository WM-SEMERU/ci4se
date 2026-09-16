def colorize(text, color=None, **kwargs):
    style = None
    bg = None
    if 'style' in kwargs:
        if kwargs['style'] not in STYLE:
            raise WrongStyle('"{}" is wrong argument for {}'.format(kwargs[
                'style'], 'style'))
        style = kwargs['style']
    if 'bg' in kwargs:
        if kwargs['bg'] not in BACKGROUND:
            raise WrongBackground('"{}" is wrong argument for {}'.format(
                kwargs['bg'], 'bg'))
        bg = kwargs['bg']
    if color not in COLOR:
        raise WrongColor('"{}" is wrong argument for {}'.format(color, 'color')
            )
    if '\x1b[0m' not in text:
        text = '\x1b[' + ';'.join([str(STYLE[style]), str(COLOR[color]),
            str(BACKGROUND[bg])]) + 'm' + text + '\x1b[0m'
    else:
        lst = text.split('\x1b[0m')
        text = ''
        for x in lst:
            if not x.startswith('\x1b['):
                x = '\x1b[' + ';'.join([str(STYLE[style]), str(COLOR[color]
                    ), str(BACKGROUND[bg])]) + 'm' + x + '\x1b[0m'
            else:
                x += '\x1b[0m'
            text += x
    return text