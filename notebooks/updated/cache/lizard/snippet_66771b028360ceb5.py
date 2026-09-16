def main(args=None):
    import argparse
    from textwrap import dedent
    parser = argparse.ArgumentParser(formatter_class=type(
        'EPCHelpFormatter', (argparse.ArgumentDefaultsHelpFormatter,
        argparse.RawDescriptionHelpFormatter), {}), description=dedent(main
        .__doc__))
    parser.add_argument('module', help='Serve python functions in this module.'
        )
    parser.add_argument('--address', default='localhost', help='server address'
        )
    parser.add_argument('--port', default=0, type=int, help=
        'server port. 0 means to pick up random port.')
    parser.add_argument('--allow-dotted-names', default=False, action=
        'store_true')
    parser.add_argument('--pdb', dest='debugger', const='pdb', action=
        'store_const', help='start pdb when error occurs.')
    parser.add_argument('--ipdb', dest='debugger', const='ipdb', action=
        'store_const', help='start ipdb when error occurs.')
    parser.add_argument('--log-traceback', action='store_true', default=False)
    ns = parser.parse_args(args)
    server = EPCServer((ns.address, ns.port), debugger=ns.debugger,
        log_traceback=ns.log_traceback)
    server.register_instance(__import__(ns.module), allow_dotted_names=ns.
        allow_dotted_names)
    server.print_port()
    server.serve_forever()