def dump(data, out, ac_parser=None, **options):
    ioi = anyconfig.ioinfo.make(out)
    psr = find(ioi, forced_type=ac_parser)
    LOGGER.info('Dumping: %s', ioi.path)
    psr.dump(data, ioi, **options)