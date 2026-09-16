def branches_containing(commit):
    lines = run('branch --contains %s' % commit).splitlines()
    return [l.lstrip('* ') for l in lines]