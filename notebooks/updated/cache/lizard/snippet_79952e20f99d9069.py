def offset_overlays(self, text, run_matchers=None, **kw):
    self._maybe_run_matchers(text, run_matchers)
    for i in self._list_match.offset_overlays(text, **kw):
        yield i