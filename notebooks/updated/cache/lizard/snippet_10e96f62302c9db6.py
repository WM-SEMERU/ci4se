def append_tier(self, coro, **kwargs):
    source = self.tiers[-1] if self.tiers else None
    return self.add_tier(coro, source=source, **kwargs)