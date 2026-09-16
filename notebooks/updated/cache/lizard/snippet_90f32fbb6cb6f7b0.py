def color(string, name, style='normal', when='auto'):
    if name not in colors:
        from .text import oxford_comma
        raise ValueError("unknown color '{}'.\nknown colors are: {}".format
            (name, oxford_comma(["'{}'".format(x) for x in sorted(colors)])))
    if style not in styles:
        from .text import oxford_comma
        raise ValueError("unknown style '{}'.\nknown styles are: {}".format
            (style, oxford_comma(["'{}'".format(x) for x in sorted(styles)])))
    prefix = '\x1b[%d;%dm' % (styles[style], colors[name])
    suffix = '\x1b[%d;%dm' % (styles['normal'], colors['normal'])
    color_string = prefix + string + suffix
    if when == 'always':
        return color_string
    elif when == 'auto':
        return color_string if sys.stdout.isatty() else string
    elif when == 'never':
        return string
    else:
        raise ValueError("when must be one of: 'always', 'auto', 'never'")