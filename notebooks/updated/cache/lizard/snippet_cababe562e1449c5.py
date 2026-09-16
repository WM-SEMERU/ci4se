def commit(self):
    self.logger.debug('Starting injections...')
    self.logger.debug('Injections dict is:')
    self.logger.debug(self.inject_dict)
    self.logger.debug('Clear list is:')
    self.logger.debug(self.clear_set)
    for filename, content in self.inject_dict.items():
        content = _unicode(content)
        self.logger.debug('Injecting values into %s...' % filename)
        self.destructive_inject(filename, content)
    for filename in self.clear_set:
        self.logger.debug('Clearing injection from %s...' % filename)
        self.destructive_clear(filename)