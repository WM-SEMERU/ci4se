def zip_bundle(tag=True):
    rev = __version__
    print('Cleaning old build files.')
    clean()
    local('mkdir -p build')
    print('Bundling new files.')
    with lcd('sphinx_bootstrap_theme/bootstrap'):
        local('zip -r ../../build/bootstrap.zip .')
    dest = os.path.abspath(os.path.join(DL_DIR, rev))
    with lcd('build'):
        local('mkdir -p %s' % dest)
        local('cp bootstrap.zip %s' % dest)
        print('Verifying contents.')
        local('unzip -l bootstrap.zip')