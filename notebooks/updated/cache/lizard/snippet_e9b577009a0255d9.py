def _cfgs_to_read(self):
    cfg = Config.DEFAULT_CONFIG_FILE_NAME
    filenames = [self.default_config_file, cfg, os.path.join(os.path.
        expanduser('~' + os.path.sep), cfg), '.pyemma.cfg']
    if self.cfg_dir:
        from glob import glob
        filenames.extend(glob(self.cfg_dir + os.path.sep + '*.cfg'))
    return filenames