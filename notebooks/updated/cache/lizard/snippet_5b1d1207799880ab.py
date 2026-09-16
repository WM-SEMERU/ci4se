def push_not_registered_user_data_task(data):
    lock_id = '%s-push-not-registered-user-data-task-%s' % (settings.
        ENV_PREFIX, data['email'])
    acquire_lock = lambda : cache.add(lock_id, 'true', LOCK_EXPIRE)
    release_lock = lambda : cache.delete(lock_id)
    if acquire_lock():
        try:
            upload_not_registered_user_data(data)
        except (KeyError, NotImplementedError, MultipleMatchingUsersError):
            release_lock()
            raise
        release_lock()