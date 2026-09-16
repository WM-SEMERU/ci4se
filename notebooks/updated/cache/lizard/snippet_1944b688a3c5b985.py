def formatcolor(string, fg=None, bg=None):
    if fg is bg is None:
        return string
    temp = (['fg=' + fg] if fg else []) + (['bg=' + bg] if bg else [])
    fmt = _color_format_parser._COLOR_DELIM.join(temp)
    return (_color_format_parser._START_TOKEN + fmt + _color_format_parser.
        _FMT_TOKEN + string + _color_format_parser._STOP_TOKEN)