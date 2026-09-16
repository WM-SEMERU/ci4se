def wait_for_task(upid, timeout=300):
    start_time = time.time()
    info = _lookup_proxmox_task(upid)
    if not info:
        log.error(
            'wait_for_task: No task information retrieved based on given criteria.'
            )
        raise SaltCloudExecutionFailure
    while True:
        if 'status' in info and info['status'] == 'OK':
            log.debug('Task has been finished!')
            return True
        time.sleep(3)
        if time.time() - start_time > timeout:
            log.debug('Timeout reached while waiting for task to be finished')
            return False
        info = _lookup_proxmox_task(upid)