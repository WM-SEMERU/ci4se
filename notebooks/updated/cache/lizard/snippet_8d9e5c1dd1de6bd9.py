def dispatch(self, stream, *args, **kwargs):
    for f, pat in self.functions:
        matched, matched_stream = self._match(stream, pat, {}, {})
        if matched:
            return f(matched_stream, *args, **kwargs)
    raise DispatchFailed()