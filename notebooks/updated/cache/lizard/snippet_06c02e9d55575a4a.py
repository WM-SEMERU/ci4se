def _load_ini(self, namespace, config_file):
    self.LOG.debug('Loading %r...' % (config_file,))
    ini_file = ConfigParser.SafeConfigParser()
    ini_file.optionxform = str
    if ini_file.read(config_file):
        self._set_from_ini(namespace, ini_file)
    else:
        self.LOG.warning(
            "Configuration file %r not found, use the command 'pyroadmin --create-config' to create it!"
             % (config_file,))