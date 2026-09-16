def _schedule_log_parsing(job, job_logs, result):
    from treeherder.log_parser.tasks import parse_logs
    task_types = {'errorsummary_json', 'buildbot_text', 'builds-4h'}
    job_log_ids = []
    for job_log in job_logs:
        if job_log.status != JobLog.PENDING:
            continue
        if job_log.name not in task_types:
            continue
        job_log_ids.append(job_log.id)
    if result != 'success':
        queue = 'log_parser_fail'
        priority = 'failures'
    else:
        queue = 'log_parser'
        priority = 'normal'
    parse_logs.apply_async(queue=queue, args=[job.id, job_log_ids, priority])