def get_repo_revision():
    repopath = _findrepo()
    if not repopath:
        return ''
    try:
        head = open(os.path.join(repopath, 'HEAD'), 'rU').read()
        for l in head.splitlines():
            l = l.split()
            if l[0] == 'ref:':
                ref = l[1]
                break
        else:
            ref = None
        if ref:
            rev = open(os.path.join(repopath, ref), 'rU').read()
            rev = rev[:7]
            if rev:
                return rev
    except IOError:
        pass
    try:
        rev = compat.exec_command('git', 'rev-parse', '--short', 'HEAD').strip(
            )
        if rev:
            return rev
    except:
        pass
    return ''