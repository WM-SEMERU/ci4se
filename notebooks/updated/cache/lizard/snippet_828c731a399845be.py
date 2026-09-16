def argv(cls, name, short_name=None, type=None, help=None):
    cls.__hierarchy.append(argv.Argv(name, short_name, type, help))