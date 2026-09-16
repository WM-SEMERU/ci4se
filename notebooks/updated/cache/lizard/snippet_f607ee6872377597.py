def refresh_core(self):
    self.log.info('Sending out mass query for all attributes')
    for key in ATTR_CORE:
        self.query(key)