def bin_pkg_info(path, saltenv='base'):
    if __salt__['config.valid_fileproto'](path):
        newpath = __salt__['cp.cache_file'](path, saltenv)
        if not newpath:
            raise CommandExecutionError(
                "Unable to retrieve {0} from saltenv '{1}'".format(path,
                saltenv))
        path = newpath
    elif not os.path.exists(path):
        raise CommandExecutionError('{0} does not exist on minion'.format(path)
            )
    elif not os.path.isabs(path):
        raise SaltInvocationError('{0} does not exist on minion'.format(path))
    queryformat = salt.utils.pkg.rpm.QUERYFORMAT.replace('%{REPOID}', 'none')
    output = __salt__['cmd.run_stdout'](['rpm', '-qp', '--queryformat',
        queryformat, path], output_loglevel='trace', ignore_retcode=True,
        python_shell=False)
    ret = {}
    pkginfo = salt.utils.pkg.rpm.parse_pkginfo(output, osarch=__grains__[
        'osarch'])
    try:
        for field in pkginfo._fields:
            ret[field] = getattr(pkginfo, field)
    except AttributeError:
        return None
    return ret