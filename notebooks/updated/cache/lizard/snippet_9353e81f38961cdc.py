def add_path(self, path, pattern='*.json'):
    if os.path.isdir(path):
        configs = glob.glob(_opj(path, pattern))
    else:
        configs = [path]
    for config in configs:
        cfg = dbconfig.DBConfig(config_file=config)
        cs = cfg.settings
        if dbconfig.DB_KEY not in cs:
            raise ValueError("No database in '{}'".format(config))
        if dbconfig.COLL_KEY in cs:
            name = '{}.{}'.format(cs[dbconfig.DB_KEY], cs[dbconfig.COLL_KEY])
        else:
            name = cs[dbconfig.DB_KEY]
        self.add(name, cfg)
    return self