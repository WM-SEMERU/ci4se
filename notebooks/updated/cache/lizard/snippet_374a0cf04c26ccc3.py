async def _populate_name_map(self):
    services = await self.sync_services()
    with self._state_lock:
        self.services = services
        for i, name in enumerate(self.services.keys()):
            self._name_map[i] = name