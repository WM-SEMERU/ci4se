def set_suffix(self):
    self.suffix = self.w.suffix.get_text()
    self.logger.debug('Output suffix set to {0}'.format(self.suffix))