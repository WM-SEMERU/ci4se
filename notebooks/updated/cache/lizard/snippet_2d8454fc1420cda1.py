def _context_wrapped(func):

    def wrapper(self, *args, **kargs):
        if type(self.context).__name__ == 'AsyncContext':
            return func(self, *args, **kargs)
        segment = DummySegment()
        self.context.set_trace_entity(segment)
        result = func(self, *args, **kargs)
        self.context.clear_trace_entities()
        return result
    return wrapper