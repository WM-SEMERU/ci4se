def vgdisplay(vgname='', quiet=False):
    ret = {}
    cmd = ['vgdisplay', '-c']
    if vgname:
        cmd.append(vgname)
    cmd_ret = __salt__['cmd.run_all'](cmd, python_shell=False,
        ignore_retcode=quiet)
    if cmd_ret['retcode'] != 0:
        return {}
    out = cmd_ret['stdout'].splitlines()
    for line in out:
        comps = line.strip().split(':')
        ret[comps[0]] = {'Volume Group Name': comps[0],
            'Volume Group Access': comps[1], 'Volume Group Status': comps[2
            ], 'Internal Volume Group Number': comps[3],
            'Maximum Logical Volumes': comps[4], 'Current Logical Volumes':
            comps[5], 'Open Logical Volumes': comps[6],
            'Maximum Logical Volume Size': comps[7],
            'Maximum Physical Volumes': comps[8],
            'Current Physical Volumes': comps[9], 'Actual Physical Volumes':
            comps[10], 'Volume Group Size (kB)': comps[11],
            'Physical Extent Size (kB)': comps[12],
            'Total Physical Extents': comps[13],
            'Allocated Physical Extents': comps[14],
            'Free Physical Extents': comps[15], 'UUID': comps[16]}
    return ret