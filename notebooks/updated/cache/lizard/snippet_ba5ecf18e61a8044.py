def reset(self, name, suppress_logging=False):
    self._close(name, suppress_logging)
    self.get(name)
    self.logger.info('Reset Flopsy Pool for {0}'.format(name))