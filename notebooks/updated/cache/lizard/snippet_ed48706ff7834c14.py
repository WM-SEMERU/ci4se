def main(argv=None):
    logging.basicConfig(level=logging.INFO)
    server_func = functools.partial(server.main, argv=argv)
    server_parser = server.attach_parser(default_subparser())
    server_parser.set_defaults(_func=server_func)
    args = default_parser().parse_args(argv)
    args._func()