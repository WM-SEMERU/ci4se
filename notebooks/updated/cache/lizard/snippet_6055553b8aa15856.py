def dump(device, destination, level=0, label=None, noerase=None):
    if not salt.utils.path.which('xfsdump'):
        raise CommandExecutionError(
            'Utility "xfsdump" has to be installed or missing.')
    label = label and label or time.strftime(
        'XFS dump for "{0}" of %Y.%m.%d, %H:%M'.format(device), time.
        localtime()).replace("'", '"')
    cmd = ['xfsdump']
    cmd.append('-F')
    if not noerase:
        cmd.append('-E')
    cmd.append("-L '{0}'".format(label))
    cmd.append('-l {0}'.format(level))
    cmd.append('-f {0}'.format(destination))
    cmd.append(device)
    cmd = ' '.join(cmd)
    out = __salt__['cmd.run_all'](cmd)
    _verify_run(out, cmd=cmd)
    return _xfsdump_output(out['stdout'])