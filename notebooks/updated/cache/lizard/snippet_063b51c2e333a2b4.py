def command(func):
    classname = inspect.getouterframes(inspect.currentframe())[1][3]
    name = func.__name__
    help_name = name.replace('do_', 'help_')
    doc = textwrap.dedent(func.__doc__)

    def new(instance, args):
        try:
            argv = shlex.split(args)
            arguments = docopt(doc, help=True, argv=argv)
            func(instance, args, arguments)
        except SystemExit:
            if args not in ('-h', '--help'):
                Console.error('Could not execute the command.')
            print(doc)
    new.__doc__ = doc
    return new