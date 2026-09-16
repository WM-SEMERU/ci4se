def task_wait(meow, heartbeat, polling_interval, timeout, task_id,
    timeout_exit_code):
    task_wait_with_io(meow, heartbeat, polling_interval, timeout, task_id,
        timeout_exit_code)