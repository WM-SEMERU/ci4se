def log_root(self):
    var_log = os.path.join(sys.prefix, 'var', 'log').replace('/usr/var', '/var'
        )
    if not os.path.isdir(var_log):
        os.makedirs(var_log)
    return var_log