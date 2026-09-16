def init():
    global _default_foreground, _default_background, _default_style
    try:
        attrs = GetConsoleScreenBufferInfo().wAttributes
    except (ArgumentError, WindowsError):
        _default_foreground = GREY
        _default_background = BLACK
        _default_style = NORMAL
    else:
        _default_foreground = attrs & 7
        _default_background = attrs >> 4 & 7
        _default_style = attrs & BRIGHT