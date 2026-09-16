def queue_jobs(main_task_path, params_list, queue=None, batch_size=1000):
    if len(params_list) == 0:
        return []
    if queue is None:
        task_def = context.get_current_config().get('tasks', {}).get(
            main_task_path) or {}
        queue = task_def.get('queue', 'default')
    from .queue import Queue
    queue_obj = Queue(queue)
    if queue_obj.is_raw:
        raise Exception("Can't queue regular jobs on a raw queue")
    all_ids = []
    for params_group in group_iter(params_list, n=batch_size):
        context.metric('jobs.status.queued', len(params_group))
        job_ids = Job.insert([{'path': main_task_path, 'params': params,
            'queue': queue, 'datequeued': datetime.datetime.utcnow(),
            'status': 'queued'} for params in params_group], w=1,
            return_jobs=False)
        all_ids += job_ids
    queue_obj.notify(len(all_ids))
    set_queues_size({queue: len(all_ids)})
    return all_ids