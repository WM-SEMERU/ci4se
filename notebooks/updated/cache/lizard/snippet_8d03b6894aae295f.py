def get_keyboard_mapping(conn):
    mn, mx = get_min_max_keycode(conn)
    return conn.core.GetKeyboardMapping(mn, mx - mn + 1)