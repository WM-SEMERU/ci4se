def release_lock(dax, key, lock_mode=LockMode.wait):
    lock_fxn = _lock_fxn('unlock', lock_mode, False)
    return dax.get_scalar(dax.callproc(lock_fxn, key if isinstance(key, (
        list, tuple)) else [key])[0])