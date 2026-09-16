def distcheck(appname='', version='', subdir=''):
    import tempfile, tarfile
    if not appname:
        appname = Utils.g_module.APPNAME
    if not version:
        version = Utils.g_module.VERSION
    waf = os.path.abspath(sys.argv[0])
    tarball = dist(appname, version)
    path = appname + '-' + version
    if os.path.exists(path):
        shutil.rmtree(path)
    t = tarfile.open(tarball)
    for x in t:
        t.extract(x)
    t.close()
    if subdir:
        build_path = os.path.join(path, subdir)
    else:
        build_path = path
    instdir = tempfile.mkdtemp('.inst', '%s-%s' % (appname, version))
    ret = Utils.pproc.Popen([waf, 'configure', 'build', 'install',
        'uninstall', '--destdir=' + instdir], cwd=build_path).wait()
    if ret:
        raise Utils.WafError('distcheck failed with code %i' % ret)
    if os.path.exists(instdir):
        raise Utils.WafError(
            'distcheck succeeded, but files were left in %s' % instdir)
    shutil.rmtree(path)