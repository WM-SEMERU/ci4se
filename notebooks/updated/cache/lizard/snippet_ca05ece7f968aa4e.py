async def set_as_default_gateway(self):
    interface = self._data['interface']
    await interface._handler.set_default_gateway(system_id=interface.node.
        system_id, id=interface.id, link_id=self.id)