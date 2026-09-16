def try_read(self, config_dir=None, **kwargs):
    if isinstance(config_dir, basestring):
        config_dir = config_dir,
    for cdir in config_dir:
        try:
            self.read(cdir, **kwargs)
            return cdir
        except IOError as e:
            pass