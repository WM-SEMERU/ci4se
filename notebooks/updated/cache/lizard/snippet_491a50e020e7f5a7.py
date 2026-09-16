def build(tasks, worker_scheduler_factory=None, detailed_summary=False, **
    env_params):
    if 'no_lock' not in env_params:
        env_params['no_lock'] = True
    luigi_run_result = _schedule_and_run(tasks, worker_scheduler_factory,
        override_defaults=env_params)
    return (luigi_run_result if detailed_summary else luigi_run_result.
        scheduling_succeeded)