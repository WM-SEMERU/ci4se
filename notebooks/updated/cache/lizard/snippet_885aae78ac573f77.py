async def init(self, name, conf=None):
    tank = self.tanks.get(name)
    if tank is not None:
        return tank
    iden = s_common.guid()
    logger.info('Creating new tank: %s', name)
    path = s_common.genpath(self.dirn, 'tanks', iden)
    tank = await CryoTank.anit(path, conf)
    node = await self.names.open((name,))
    await node.set((iden, conf))
    self.tanks.put(name, tank)
    return tank