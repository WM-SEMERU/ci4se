def load_window_settings(self, prefix, default=False, section='main'):
    get_func = CONF.get_default if default else CONF.get
    window_size = get_func(section, prefix + 'size')
    prefs_dialog_size = get_func(section, prefix + 'prefs_dialog_size')
    if default:
        hexstate = None
    else:
        hexstate = get_func(section, prefix + 'state', None)
    pos = get_func(section, prefix + 'position')
    width = pos[0]
    height = pos[1]
    screen_shape = QApplication.desktop().geometry()
    current_width = screen_shape.width()
    current_height = screen_shape.height()
    if current_width < width or current_height < height:
        pos = CONF.get_default(section, prefix + 'position')
    is_maximized = get_func(section, prefix + 'is_maximized')
    is_fullscreen = get_func(section, prefix + 'is_fullscreen')
    return (hexstate, window_size, prefs_dialog_size, pos, is_maximized,
        is_fullscreen)