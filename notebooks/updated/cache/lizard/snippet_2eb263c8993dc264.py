def start(self, start_context):
    for p in self._providers:
        p.start(start_context)
    if self._clear_start:
        self.clear_cache()