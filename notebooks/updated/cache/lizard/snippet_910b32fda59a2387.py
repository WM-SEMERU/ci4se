def ssh(cls, vm_id, login, identity, args=None):
    cmd = ['ssh']
    if identity:
        cmd.extend(('-i', identity))
    version, ip_addr = cls.vm_ip(vm_id)
    if version == 6:
        cmd.append('-6')
    if not ip_addr:
        cls.echo('No IP address found for vm %s, aborting.' % vm_id)
        return
    cmd.append('%s@%s' % (login, ip_addr))
    if args:
        cmd.extend(args)
    cls.echo('Requesting access using: %s ...' % ' '.join(cmd))
    return cls.execute(cmd, False)