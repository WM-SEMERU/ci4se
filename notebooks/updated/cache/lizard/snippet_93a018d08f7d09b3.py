def begin_span(self, name, span_type, context=None, leaf=False, tags=None):
    return self._begin_span(name, span_type, context=context, leaf=leaf,
        tags=tags, parent_span_id=None)