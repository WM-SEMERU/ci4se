def parse_cmdline(argparser_):
    opts = argparser_.parse_args()
    if not opts.server:
        argparser_.error('No WBEM server specified')
        return None
    return opts