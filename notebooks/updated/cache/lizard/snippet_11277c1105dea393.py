async def probe(self):
    for adapter in self.adapters:
        if adapter.get_config('probe_supported', False):
            await adapter.probe()