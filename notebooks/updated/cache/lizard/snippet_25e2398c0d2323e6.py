def install(self, version, upgrade=False):
    print('Installing version: ' + colorize('info', version))
    self.make_lib(version)
    self.make_bin()
    self.make_env()
    self.update_path()
    return 0