async def addCharm(self, charm, series):
    if charm.startswith('local:'):
        return charm
    entity_id = await self.charmstore.entityId(charm)
    log.debug('Adding %s', entity_id)
    await self.client_facade.AddCharm(None, entity_id)
    return entity_id