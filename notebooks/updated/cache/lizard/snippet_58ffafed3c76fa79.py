def list_upgrades(refresh=True, **kwargs):
    jail = kwargs.pop('jail', None)
    chroot = kwargs.pop('chroot', None)
    root = kwargs.pop('root', None)
    fromrepo = kwargs.pop('fromrepo', None)
    cmd = _pkg(jail, chroot, root)
    cmd.extend(['upgrade', '--dry-run', '--quiet'])
    if not refresh:
        cmd.append('--no-repo-update')
    if fromrepo:
        cmd.extend(['--repository', fromrepo])
    out = __salt__['cmd.run_stdout'](cmd, output_loglevel='trace',
        python_shell=False, ignore_retcode=True)
    return {pkgname: pkgstat['version']['new'] for pkgname, pkgstat in six.
        iteritems(_parse_upgrade(out)['upgrade'])}