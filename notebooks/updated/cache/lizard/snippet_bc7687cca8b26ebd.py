def get_translation_dicts(self):
    keysym_to_string_dict = {}
    string_to_keysym_dict = {}
    Xlib.XK.load_keysym_group('latin2')
    Xlib.XK.load_keysym_group('latin3')
    Xlib.XK.load_keysym_group('latin4')
    Xlib.XK.load_keysym_group('greek')
    for string, keysym in Xlib.XK.__dict__.items():
        if string.startswith('XK_'):
            string_to_keysym_dict[string[3:]] = keysym
            keysym_to_string_dict[keysym] = string[3:]
    return keysym_to_string_dict, string_to_keysym_dict