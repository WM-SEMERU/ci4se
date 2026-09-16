def parse_pac_file(pacfile):
    try:
        with open(pacfile) as f:
            pac_script = f.read()
            _pacparser.parse_pac_string(pac_script)
    except IOError:
        raise IOError('Could not read the pacfile: {}'.format(pacfile))