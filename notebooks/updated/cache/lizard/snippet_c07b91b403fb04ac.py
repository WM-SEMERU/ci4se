def profile(name='stats', _stats=stats):

    def _profile(function):

        def __profile(*args, **kw):
            start_time = timer()
            start_memory = _get_memory_usage()
            try:
                return function(*args, **kw)
            finally:
                total = timer() - start_time
                kstones = _seconds_to_kpystones(total)
                memory = _get_memory_usage() - start_memory
                _stats[name] = {'time': total, 'kstones': kstones, 'memory':
                    memory}
        return __profile
    return _profile