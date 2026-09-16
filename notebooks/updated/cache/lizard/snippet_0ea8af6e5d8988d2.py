def pausable_restart_on_change(restart_map, stopstart=False,
    restart_functions=None):

    def wrap(f):
        __restart_map_cache = {'cache': None}

        @functools.wraps(f)
        def wrapped_f(*args, **kwargs):
            if is_unit_paused_set():
                return f(*args, **kwargs)
            if __restart_map_cache['cache'] is None:
                __restart_map_cache['cache'] = restart_map() if callable(
                    restart_map) else restart_map
            return restart_on_change_helper(lambda : f(*args, **kwargs),
                __restart_map_cache['cache'], stopstart, restart_functions)
        return wrapped_f
    return wrap