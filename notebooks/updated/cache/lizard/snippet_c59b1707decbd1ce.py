def src_file(self):
    try:
        src_uri = (curl[Gentoo._LATEST_TXT] | tail['-n', '+3'] | cut['-f1',
            '-d '])().strip()
    except ProcessExecutionError as proc_ex:
        src_uri = 'NOT-FOUND'
        LOG.error('Could not determine latest stage3 src uri: %s', str(proc_ex)
            )
    return src_uri