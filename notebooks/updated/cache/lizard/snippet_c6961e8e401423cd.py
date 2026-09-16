def remove_global_hook(handler):
    for i, cb in enumerate(state.global_hooks):
        cb = cb()
        if cb is not None and cb is handler:
            state.global_hooks.pop(i)
            log.info('removing a global hook callback')
            return True
    return False