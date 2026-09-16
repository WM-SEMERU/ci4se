def _do_download(version, download_base, to_dir, download_delay):
    py_desig = 'py{sys.version_info[0]}.{sys.version_info[1]}'.format(sys=sys)
    tp = 'setuptools-{version}-{py_desig}.egg'
    egg = os.path.join(to_dir, tp.format(**locals()))
    if not os.path.exists(egg):
        archive = download_setuptools(version, download_base, to_dir,
            download_delay)
        _build_egg(egg, archive, to_dir)
    sys.path.insert(0, egg)
    if 'pkg_resources' in sys.modules:
        _unload_pkg_resources()
    import setuptools
    setuptools.bootstrap_install_from = egg