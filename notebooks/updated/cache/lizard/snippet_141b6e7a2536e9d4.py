async def expose(self, application):
    application = self.resolve(application)
    log.info('Exposing %s', application)
    return await self.model.applications[application].expose()