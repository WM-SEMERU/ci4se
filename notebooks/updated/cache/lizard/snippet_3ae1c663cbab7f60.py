def old_streamer(main_method):
    if not arguments:
        return [sys.stdin]
    elif arguments[0] == '-c':
        return [StringIO(get_clipboard_data())]
    for argument in arguments:
        if os.path.isfile(argument):
            return file(argument, 'r')
    return method