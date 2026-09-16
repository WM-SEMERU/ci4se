def list_domains():
    vms = []
    cmd = 'vagrant global-status'
    reply = __salt__['cmd.shell'](cmd)
    log.info('--->\n%s', reply)
    for line in reply.split('\n'):
        tokens = line.strip().split()
        try:
            _ = int(tokens[0], 16)
        except (ValueError, IndexError):
            continue
        machine = tokens[1]
        cwd = tokens[-1]
        name = get_machine_id(machine, cwd)
        if name:
            vms.append(name)
    return vms