def run(self, module, options):
    logger.debug('Running maintainability harvester')
    return dict(self.harvester.results)