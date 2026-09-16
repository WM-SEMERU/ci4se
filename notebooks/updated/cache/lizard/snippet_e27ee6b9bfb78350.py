def __add_kickoff_task(cls, job_config, mapreduce_spec):
    params = {'mapreduce_id': job_config.job_id}
    kickoff_task = taskqueue.Task(url=job_config._base_path +
        '/kickoffjob_callback/' + job_config.job_id, headers=util.
        _get_task_headers(job_config.job_id), params=params)
    if job_config._hooks_cls:
        hooks = job_config._hooks_cls(mapreduce_spec)
        try:
            hooks.enqueue_kickoff_task(kickoff_task, job_config.queue_name)
            return
        except NotImplementedError:
            pass
    kickoff_task.add(job_config.queue_name, transactional=True)