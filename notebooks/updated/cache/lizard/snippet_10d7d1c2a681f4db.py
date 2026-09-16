def _init_config(self):
    system = platform.system().lower()
    leveldb_fallback_dir = os.path.expanduser('~')
    if system.startswith('darwin'):
        leveldb_fallback_dir = os.path.join(leveldb_fallback_dir, 'Library',
            'Ethereum')
    elif system.startswith('windows'):
        leveldb_fallback_dir = os.path.join(leveldb_fallback_dir, 'AppData',
            'Roaming', 'Ethereum')
    else:
        leveldb_fallback_dir = os.path.join(leveldb_fallback_dir, '.ethereum')
    leveldb_fallback_dir = os.path.join(leveldb_fallback_dir, 'geth',
        'chaindata')
    if not os.path.exists(self.config_path):
        log.info('No config file found. Creating default: ' + self.config_path)
        open(self.config_path, 'a').close()
    config = ConfigParser(allow_no_value=True)
    config.optionxform = str
    config.read(self.config_path, 'utf-8')
    if 'defaults' not in config.sections():
        self._add_default_options(config)
    if not config.has_option('defaults', 'leveldb_dir'):
        self._add_leveldb_option(config, leveldb_fallback_dir)
    if not config.has_option('defaults', 'dynamic_loading'):
        self._add_dynamic_loading_option(config)
    with codecs.open(self.config_path, 'w', 'utf-8') as fp:
        config.write(fp)
    leveldb_dir = config.get('defaults', 'leveldb_dir', fallback=
        leveldb_fallback_dir)
    return os.path.expanduser(leveldb_dir)