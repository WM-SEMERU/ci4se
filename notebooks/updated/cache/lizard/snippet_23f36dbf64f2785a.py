def install_ruby(ruby, runas=None, opts=None, env=None):
    if opts is None:
        opts = []
    if runas and runas != 'root':
        _rvm(['autolibs', 'disable', ruby] + opts, runas=runas)
        opts.append('--disable-binary')
    return _rvm(['install', ruby] + opts, runas=runas, env=env)