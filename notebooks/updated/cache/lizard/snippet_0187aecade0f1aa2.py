def acquires_lock(expires, should_fail=True, should_wait=False, resource=
    None, prefix=DEFAULT_PREFIX):
    if isinstance(expires, timedelta):
        expires = expires.total_seconds()

    def decorator(f):
        nonlocal resource
        if resource is None:
            resource = f.__name__
        resource = '%s%s' % (prefix, resource)

        @wraps(f)
        def wrapper(*args, **kwargs):
            lock = redis_lock.Lock(_redis_conn, resource, expire=expires)
            lock_acquired = False
            nonlocal should_wait
            is_blocking = should_wait
            should_execute_if_lock_fails = False
            if 'should_execute_if_lock_fails' in kwargs:
                should_execute_if_lock_fails = kwargs.pop(
                    'should_execute_if_lock_fails')
            if 'should_wait' in kwargs:
                is_blocking = kwargs.pop('should_wait')
                if is_blocking:
                    logger.debug('Waiting for resource "%s"', resource)
            if not lock.acquire(blocking=is_blocking):
                if should_fail:
                    raise RuntimeError('Failed to acquire lock: %s' % resource)
                logger.warning('Failed to acquire lock: %s', resource)
                if not should_execute_if_lock_fails:
                    return False
            else:
                lock_acquired = True
            try:
                return f(*args, **kwargs)
            finally:
                try:
                    if lock_acquired:
                        lock.release()
                except Exception as e:
                    logger.exception('Failed to release lock: %s', str(e),
                        exc_info=False)
        return wrapper
    return decorator