def _parser_options():
    import argparse
    from acorn import base
    pdescr = 'ACORN setup and custom configuration'
    parser = argparse.ArgumentParser(parents=[base.bparser], description=pdescr
        )
    for arg, options in script_options.items():
        parser.add_argument(arg, **options)
    args = base.exhandler(examples, parser)
    if args is None:
        return
    return args