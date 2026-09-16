def make(self, apps):
    for subreport in self.subreports:
        logger.debug('Make subreport "{0}"'.format(subreport.name))
        subreport.make(apps)
    for subreport in self.subreports:
        subreport.compact_tables()