def fetch(name, jail=None, chroot=None, root=None, fetch_all=False, quiet=
    False, fromrepo=None, glob=True, regex=False, pcre=False, local=False,
    depends=False):
    opts = ''
    if fetch_all:
        opts += 'a'
    if quiet:
        opts += 'q'
    if glob:
        opts += 'g'
    if regex:
        opts += 'x'
    if pcre:
        opts += 'X'
    if local:
        opts += 'L'
    if depends:
        opts += 'd'
    cmd = _pkg(jail, chroot, root)
    cmd.extend(['fetch', '-y'])
    if fromrepo:
        cmd.extend(['-r', fromrepo])
    if opts:
        cmd.append('-' + opts)
    cmd.append(name)
    return __salt__['cmd.run'](cmd, output_loglevel='trace', python_shell=False
        )