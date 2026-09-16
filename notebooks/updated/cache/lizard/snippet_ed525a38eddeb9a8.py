def print_error_messages_raylet(task_error_queue, threads_stopped):
    while True:
        if threads_stopped.is_set():
            return
        try:
            error, t = task_error_queue.get(block=False)
        except queue.Empty:
            threads_stopped.wait(timeout=0.01)
            continue
        while t + UNCAUGHT_ERROR_GRACE_PERIOD > time.time():
            threads_stopped.wait(timeout=1)
            if threads_stopped.is_set():
                break
        if t < last_task_error_raise_time + UNCAUGHT_ERROR_GRACE_PERIOD:
            logger.debug('Suppressing error from worker: {}'.format(error))
        else:
            logger.error('Possible unhandled error from worker: {}'.format(
                error))