def conda_prefix(user=None):
    if user == 'root':
        return __salt__['grains.get']('conda:prefix', default='/opt/anaconda')
    else:
        if user is None:
            user = __salt__['pillar.get']('system:user', 'ubuntu')
        for u in pwd.getpwall():
            if u.pw_name == user:
                return os.path.join(u.pw_dir, 'anaconda')