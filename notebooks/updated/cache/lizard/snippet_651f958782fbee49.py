def make_pkgng_aware(jname):
    ret = {'changes': {}}
    cdir = _config_dir()
    if not os.path.isdir(cdir):
        os.makedirs(cdir)
        if os.path.isdir(cdir):
            ret['changes'] = 'Created poudriere make file dir {0}'.format(cdir)
        else:
            return 'Could not create or find required directory {0}'.format(
                cdir)
    __salt__['file.write']('{0}-make.conf'.format(os.path.join(cdir, jname)
        ), 'WITH_PKGNG=yes')
    if os.path.isfile(os.path.join(cdir, jname) + '-make.conf'):
        ret['changes'] = 'Created {0}'.format(os.path.join(cdir,
            '{0}-make.conf'.format(jname)))
        return ret
    else:
        return 'Looks like file {0} could not be created'.format(os.path.
            join(cdir, jname + '-make.conf'))