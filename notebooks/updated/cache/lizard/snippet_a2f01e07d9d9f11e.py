def add_mutex_switch(parser, dest, arguments=set(), default=None,
    single_arg=False, required=False):
    if default is not None:
        assert default in arguments
    if isinstance(arguments, set):
        arguments = {k: None for k in arguments}
    if not single_arg:
        mg = parser.add_mutually_exclusive_group(required=required)
        for name, help_text in arguments.items():
            kwargs = {'action': 'store_const', 'dest': dest, 'const': name,
                'help': help_text}
            if default == name:
                kwargs['default'] = name
            mg.add_argument('--{}'.format(name), **kwargs)
        return mg
    else:
        kwargs = {'dest': dest, 'type': str, 'default': default, 'help':
            '\n'.join('{}: {}'.format(k, v) for k, v in arguments.items()),
            'choices': list(arguments.keys())}
        return parser.add_argument('--{}'.format(dest), **kwargs)