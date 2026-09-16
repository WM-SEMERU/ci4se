def bg_color_native_ansi(kernel32, stderr, stdout):
    try:
        if stderr == INVALID_HANDLE_VALUE:
            raise OSError
        bg_color, native_ansi = get_console_info(kernel32, stderr)[1:]
    except OSError:
        try:
            if stdout == INVALID_HANDLE_VALUE:
                raise OSError
            bg_color, native_ansi = get_console_info(kernel32, stdout)[1:]
        except OSError:
            bg_color, native_ansi = WINDOWS_CODES['black'], False
    return bg_color, native_ansi