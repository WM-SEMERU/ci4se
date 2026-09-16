def values(self):
    logger.debug('call values')
    return [self.get(key) for key in self.keys()]