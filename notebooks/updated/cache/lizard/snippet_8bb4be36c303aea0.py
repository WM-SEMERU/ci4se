def help_message():
    parser = autopep8.create_parser()
    string_io = io.StringIO()
    parser.print_help(string_io)
    return string_io.getvalue().replace(os.path.expanduser('~'), '~')