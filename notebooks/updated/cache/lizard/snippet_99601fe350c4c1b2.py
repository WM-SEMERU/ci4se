def _wait_for_spot_instance(update_callback, update_args=None,
    update_kwargs=None, timeout=10 * 60, interval=30, interval_multiplier=1,
    max_failures=10):
    if update_args is None:
        update_args = ()
    if update_kwargs is None:
        update_kwargs = {}
    duration = timeout
    while True:
        log.debug(
            'Waiting for spot instance reservation. Giving up in 00:%02d:%02d',
            int(timeout // 60), int(timeout % 60))
        data = update_callback(*update_args, **update_kwargs)
        if data is False:
            log.debug(
                'update_callback has returned False which is considered a failure. Remaining Failures: %s'
                , max_failures)
            max_failures -= 1
            if max_failures <= 0:
                raise SaltCloudExecutionFailure(
                    'Too many failures occurred while waiting for the spot instance reservation to become active.'
                    )
        elif data is not None:
            return data
        if timeout < 0:
            raise SaltCloudExecutionTimeout(
                'Unable to get an active spot instance request for 00:{0:02d}:{1:02d}'
                .format(int(duration // 60), int(duration % 60)))
        time.sleep(interval)
        timeout -= interval
        if interval_multiplier > 1:
            interval *= interval_multiplier
            if interval > timeout:
                interval = timeout + 1
            log.info('Interval multiplier in effect; interval is now %ss',
                interval)