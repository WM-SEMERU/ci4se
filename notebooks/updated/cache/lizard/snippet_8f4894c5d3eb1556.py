def delete_jail(name):
    if is_jail(name):
        cmd = 'poudriere jail -d -j {0}'.format(name)
        __salt__['cmd.run'](cmd)
        if is_jail(name):
            return (
                'Looks like there was an issue deleteing jail             {0}'
                .format(name))
    else:
        return 'Looks like jail {0} has not been created'.format(name)
    make_file = os.path.join(_config_dir(), '{0}-make.conf'.format(name))
    if os.path.isfile(make_file):
        try:
            os.remove(make_file)
        except (IOError, OSError):
            return (
                'Deleted jail "{0}" but was unable to remove jail make file'
                .format(name))
        __salt__['file.remove'](make_file)
    return 'Deleted jail {0}'.format(name)