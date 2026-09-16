def wrap(self, encoding, **textio_args):
    if ('line_buffering' not in textio_args and 'write_through' not in
        textio_args):
        textio_args['write_through'] = True
    return compat.TextIOWrapper(self, encoding, **textio_args)