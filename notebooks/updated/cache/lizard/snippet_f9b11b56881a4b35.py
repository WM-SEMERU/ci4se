def log(self, message, level='info'):
    getattr(self.logger, level)('[%s] %s' % (self.id, message))