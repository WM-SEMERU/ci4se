def get_application(self, id=None, name=None):
    log.info('Picking application: %s (%s)' % (name, id))
    return self.applications[id or name]