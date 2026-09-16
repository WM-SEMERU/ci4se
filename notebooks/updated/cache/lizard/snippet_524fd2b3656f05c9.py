def encompasses(self, span):
    if isinstance(span, list):
        return [sp for sp in span if self._encompasses(sp)]
    return self._encompasses(span)