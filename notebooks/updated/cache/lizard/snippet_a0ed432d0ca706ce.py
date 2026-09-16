async def addRelation(self, endpoint1, endpoint2):
    endpoints = [endpoint1, endpoint2]
    for i in range(len(endpoints)):
        parts = endpoints[i].split(':')
        parts[0] = self.resolve(parts[0])
        endpoints[i] = ':'.join(parts)
    log.info('Relating %s <-> %s', *endpoints)
    return await self.model.add_relation(*endpoints)