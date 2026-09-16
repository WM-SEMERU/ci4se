def list_sebool():
    bdata = __salt__['cmd.run']('semanage boolean -l').splitlines()
    ret = {}
    for line in bdata[1:]:
        if not line.strip():
            continue
        comps = line.split()
        ret[comps[0]] = {'State': comps[1][1:], 'Default': comps[3][:-1],
            'Description': ' '.join(comps[4:])}
    return ret