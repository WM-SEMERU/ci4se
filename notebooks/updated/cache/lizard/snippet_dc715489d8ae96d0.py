def _add_var(var, value):
    makeconf = _get_makeconf()
    layman = 'source /var/lib/layman/make.conf'
    fullvar = '{0}="{1}"'.format(var, value)
    if __salt__['file.contains'](makeconf, layman):
        cmd = ['sed', '-i', '/{0}/ i\\{1}'.format(layman.replace('/', '\\/'
            ), fullvar), makeconf]
        __salt__['cmd.run'](cmd)
    else:
        __salt__['file.append'](makeconf, fullvar)