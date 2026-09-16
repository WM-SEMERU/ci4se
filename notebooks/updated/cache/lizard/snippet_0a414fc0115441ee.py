def qos(self, prefetch_size=0, prefetch_count=0, apply_global=False):
    return self.backend.qos(prefetch_size, prefetch_count, apply_global)