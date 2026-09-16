def appendpickle(table, source=None, protocol=-1, write_header=False):
    _writepickle(table, source=source, mode='ab', protocol=protocol,
        write_header=write_header)