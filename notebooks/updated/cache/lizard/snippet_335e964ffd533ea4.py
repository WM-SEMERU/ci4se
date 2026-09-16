def register(self, handler, filters=None, index=None):
    from .filters import get_filters_spec
    spec, handler = _get_spec(handler)
    if filters and not isinstance(filters, (list, tuple, set)):
        filters = [filters]
    filters = get_filters_spec(self.dispatcher, filters)
    record = Handler.HandlerObj(handler=handler, spec=spec, filters=filters)
    if index is None:
        self.handlers.append(record)
    else:
        self.handlers.insert(index, record)