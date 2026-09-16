def pull(args):
    p = OptionParser(pull.__doc__)
    opts, args = p.parse_args(args)
    if len(args) != 3:
        sys.exit(not p.print_help())
    prefix = get_prefix()
    version, partID, unitigID = args
    s = '.'.join(args)
    cmd = 'tigStore'
    cmd += ' -g ../{0}.gkpStore -t ../{0}.tigStore'.format(prefix)
    cmd += ' {0} -up {1} -d layout -u {2}'.format(version, partID, unitigID)
    unitigfile = 'unitig' + s
    sh(cmd, outfile=unitigfile)
    return unitigfile