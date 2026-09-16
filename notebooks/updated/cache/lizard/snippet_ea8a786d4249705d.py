def pretty_exe_doc(program, parser, stack=1, under='-'):
    if os.path.basename(sys.argv[0]) == 'sphinx-build':
        mod = inspect.getmodule(inspect.stack()[stack][0])
        _parser = parser() if '__call__' in dir(parser) else parser
        _parser.set_usage(mod.__usage__.replace('%prog', program))
        mod.__doc__ = '\n'.join(['', program, under * len(program), '::',
            ''] + [('    %s' % l) for l in _parser.format_help().split('\n')]
            ) + mod.__doc__