def trace_emit(self):

    def decorator(f):
        self.tracer.emitter = f
        return f
    return decorator