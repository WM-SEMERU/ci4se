def _logStormQuery(self, text, user):
    if self.conf.get('storm:log'):
        lvl = self.conf.get('storm:log:level')
        logger.log(lvl, 'Executing storm query {%s} as [%s]', text, user.name)