def on_retry(self, exc, task_id, args, kwargs, einfo):
    super(LoggedTask, self).on_retry(exc, task_id, args, kwargs, einfo)
    log.warning('[{}] retried due to {}'.format(task_id, getattr(einfo,
        'traceback', None)))