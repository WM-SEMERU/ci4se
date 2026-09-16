def _linux_remotes_on(port, which_end):
    remotes = set()
    try:
        data = subprocess.check_output(['lsof', '-iTCP:{0:d}'.format(port),
            '-n', '-P'])
    except subprocess.CalledProcessError as ex:
        if ex.returncode == 1:
            log.warning('"lsof" returncode = 1, likely no active TCP sessions.'
                )
            return remotes
        log.error('Failed "lsof" with returncode = %s', ex.returncode)
        raise
    lines = salt.utils.stringutils.to_str(data).split('\n')
    for line in lines:
        chunks = line.split()
        if not chunks:
            continue
        if 'COMMAND' in chunks[0]:
            continue
        if 'ESTABLISHED' not in chunks[-1]:
            continue
        local, remote = chunks[8].split('->')
        _, lport = local.rsplit(':', 1)
        rhost, rport = remote.rsplit(':', 1)
        if which_end == 'remote_port' and int(rport) != port:
            continue
        if which_end == 'local_port' and int(lport) != port:
            continue
        remotes.add(rhost.strip('[]'))
    return remotes