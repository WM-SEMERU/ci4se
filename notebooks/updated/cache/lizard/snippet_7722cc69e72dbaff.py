def dispatch_strict(self, stream, *args, **kwargs):
    for f, pat in self.functions:
        matched, matched_stream = self._match(stream, pat, {'strict': True}, {}
            )
        if matched:
            return f(matched_stream, *args, **kwargs)
    raise DispatchFailed()