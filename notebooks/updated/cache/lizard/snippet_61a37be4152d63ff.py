def list_active_vms(cwd=None):
    vms = []
    cmd = 'vagrant status'
    reply = __salt__['cmd.shell'](cmd, cwd=cwd)
    log.info('--->\n%s', reply)
    for line in reply.split('\n'):
        tokens = line.strip().split()
        if len(tokens) > 1:
            if tokens[1] == 'running':
                vms.append(tokens[0])
    return vms