def _parse_args(cls):
    cls.parser = argparse.ArgumentParser()
    cls.parser.add_argument('symbol', help='Symbol for horizontal line',
        nargs='*')
    cls.parser.add_argument('--color', '-c', help='Color of the line',
        default=None, nargs=1)
    cls.parser.add_argument('--version', '-v', action='version', version='0.13'
        )
    return cls.parser