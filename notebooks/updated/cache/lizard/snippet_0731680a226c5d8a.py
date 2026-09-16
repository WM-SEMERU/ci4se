def experiment_group_pre_delete(sender, **kwargs):
    instance = kwargs['instance']
    if instance.is_selection:
        return
    celery_app.send_task(SchedulerCeleryTasks.
        STORES_SCHEDULE_OUTPUTS_DELETION, kwargs={'persistence': instance.
        persistence_outputs, 'subpath': instance.subpath}, countdown=conf.
        get('GLOBAL_COUNTDOWN'))
    celery_app.send_task(SchedulerCeleryTasks.STORES_SCHEDULE_LOGS_DELETION,
        kwargs={'persistence': instance.persistence_logs, 'subpath':
        instance.subpath}, countdown=conf.get('GLOBAL_COUNTDOWN'))