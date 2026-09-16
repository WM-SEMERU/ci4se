def save_new_environment(name, datadir, srcdir, ckan_version, deploy_target
    =None, always_prod=False):
    with open(datadir + '/.version', 'w') as f:
        f.write('2')
    cp = ConfigParser.SafeConfigParser()
    cp.read(srcdir + '/.datacats-environment')
    if not cp.has_section('datacats'):
        cp.add_section('datacats')
    cp.set('datacats', 'name', name)
    cp.set('datacats', 'ckan_version', ckan_version)
    if deploy_target:
        if not cp.has_section('deploy'):
            cp.add_section('deploy')
        cp.set('deploy', 'target', deploy_target)
    if always_prod:
        cp.set('datacats', 'always_prod', 'true')
    with open(srcdir + '/.datacats-environment', 'w') as config:
        cp.write(config)
    save_srcdir_location(datadir, srcdir)