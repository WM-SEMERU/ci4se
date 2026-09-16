def setup_logging(self, defaults=None):
    if 'loggers' in self.get_sections():
        defaults = self._get_defaults(defaults)
        fileConfig(self.uri.path, defaults, disable_existing_loggers=False)
    else:
        logging.basicConfig()