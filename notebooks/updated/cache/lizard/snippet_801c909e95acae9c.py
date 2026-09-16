def critical_section_lock(lock=None, blocking=True, timeout=None,
    raise_exception=True):

    def lock_getter(*args, **kwargs):
        return lock
    return critical_section_dynamic_lock(lock_fn=lock_getter, blocking=
        blocking, timeout=timeout, raise_exception=raise_exception)