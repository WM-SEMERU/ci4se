def pkgconfig(*packages, **kw):
    config = kw.setdefault('config', {})
    optional_args = kw.setdefault('optional', '')
    flag_map = {'include_dirs': ['--cflags-only-I', 2], 'library_dirs': [
        '--libs-only-L', 2], 'libraries': ['--libs-only-l', 2],
        'extra_compile_args': ['--cflags-only-other', 0], 'extra_link_args':
        ['--libs-only-other', 0]}
    for package in packages:
        for distutils_key, (pkg_option, n) in flag_map.items():
            items = subprocess.check_output(['pkg-config', optional_args,
                pkg_option, package]).decode('utf8').split()
            config.setdefault(distutils_key, []).extend([i[n:] for i in items])
    return config