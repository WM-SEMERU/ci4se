def remove_local_exception_handler(handler, coro=None):
    if coro is None:
        coro = compat.getcurrent()
    for i, cb in enumerate(state.local_exception_handlers.get(coro, [])):
        cb = cb()
        if cb is not None and cb is handler:
            state.local_exception_handlers[coro].pop(i)
            log.info('removing a coroutine local exception handler')
            return True
    return False