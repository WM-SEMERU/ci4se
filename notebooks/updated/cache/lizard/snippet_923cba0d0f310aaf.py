def rtouches(self, span):
    if isinstance(span, list):
        return [sp for sp in span if self._rtouches(sp)]
    return self._rtouches(span)