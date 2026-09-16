def get_environment(self, id=None, name=None):
    log.info('Picking environment: %s (%s)' % (name, id))
    return self.environments[id or name]