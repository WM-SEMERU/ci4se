def check_usage(docstring, argv=None, usageifnoargs=False):
    if argv is None:
        from sys import argv
    if len(argv) == 1 and usageifnoargs:
        show_usage(docstring, usageifnoargs != 'long', None, 0)
    if len(argv) == 2 and argv[1] in ('-h', '--help'):
        show_usage(docstring, False, None, 0)