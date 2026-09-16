def check_perms(self, perms='0600,0400'):
    confpath = os.path.realpath(self.config_file)
    mode = stat.S_IMODE(os.stat(confpath).st_mode)
    if not any([(mode == int(i, 8)) for i in perms.split(',')]):
        msg = (
            'To use a configuration file the permissions need to be any of the following "%s"'
             % perms)
        self.log.fatal(msg)
        raise SystemExit(msg)
    else:
        self.log.info('Configuration file [ %s ] has been loaded', self.
            config_file)
        return True