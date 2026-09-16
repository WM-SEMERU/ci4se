def detail(device='/dev/md0'):
    ret = {}
    ret['members'] = {}
    if not os.path.exists(device):
        msg = "Device {0} doesn't exist!"
        raise CommandExecutionError(msg.format(device))
    cmd = ['mdadm', '--detail', device]
    for line in __salt__['cmd.run_stdout'](cmd, python_shell=False).splitlines(
        ):
        if line.startswith(device):
            continue
        if ' ' not in line:
            continue
        if ':' not in line:
            if '/dev/' in line:
                comps = line.split()
                state = comps[4:-1]
                ret['members'][comps[0]] = {'device': comps[-1], 'major':
                    comps[1], 'minor': comps[2], 'number': comps[0],
                    'raiddevice': comps[3], 'state': ' '.join(state)}
            continue
        comps = line.split(' : ')
        comps[0] = comps[0].lower()
        comps[0] = comps[0].strip()
        comps[0] = comps[0].replace(' ', '_')
        ret[comps[0]] = comps[1].strip()
    return ret