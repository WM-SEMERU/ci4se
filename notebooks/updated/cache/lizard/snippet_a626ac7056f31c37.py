def get_limits(self):
    logger.debug('Getting limits for Lambda')
    if self.limits != {}:
        return self.limits
    self._construct_limits()
    return self.limits