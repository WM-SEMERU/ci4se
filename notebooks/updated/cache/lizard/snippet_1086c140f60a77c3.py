def _run_async_task(task=None, session=None):
    if task is None or session is None:
        return None
    task_name = session.xenapi.task.get_name_label(task)
    log.debug('Running %s', task_name)
    while session.xenapi.task.get_status(task) == 'pending':
        progress = round(session.xenapi.task.get_progress(task), 2) * 100
        log.debug('Task progress %.2f%%', progress)
        time.sleep(1)
    log.debug('Cleaning up task %s', task_name)
    session.xenapi.task.destroy(task)