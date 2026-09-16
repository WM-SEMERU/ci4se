def _acquire_lock_and_execute(lock_manager: ConsulLockManager,
    configuration: CliLockAndExecuteConfiguration):
    lock = _acquire_lock(lock_manager, configuration)
    if lock is None:
        exit(UNABLE_TO_ACQUIRE_LOCK_EXIT_CODE)
    return_code, _, _ = lock_manager.execute_with_lock(configuration.
        executable, lock)
    exit(return_code)