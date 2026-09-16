def get_current_span():
    context = RequestContextManager.current_context()
    if context is not None:
        return context.span
    active = opentracing.tracer.scope_manager.active
    return active.span if active else None