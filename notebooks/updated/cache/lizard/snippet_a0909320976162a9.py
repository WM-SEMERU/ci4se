def status_subversion(path, ignore_set, options):
    subrepos = ()
    if path in ignore_set:
        return None, subrepos
    keepers = []
    for line in run(['svn', 'st', '-v'], cwd=path):
        if not line.strip():
            continue
        if line.startswith(b'Performing') or line[0] in b'X?':
            continue
        status = line[:8]
        ignored_states = options.ignore_svn_states
        if ignored_states and status.strip() in ignored_states:
            continue
        filename = line[8:].split(None, 3)[-1]
        ignore_set.add(os.path.join(path, filename))
        if status.strip():
            keepers.append(b' ' + status + filename)
    return keepers, subrepos