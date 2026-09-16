def stats():
    ret = {}
    out = __salt__['cmd.run']('quotastats').splitlines()
    for line in out:
        if not line:
            continue
        comps = line.split(': ')
        ret[comps[0]] = comps[1]
    return ret