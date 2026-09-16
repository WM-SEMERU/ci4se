def rintersects(self, span):
    if isinstance(span, list):
        return [sp for sp in span if self._rintersects(sp)]
    return self._rintersects(span)