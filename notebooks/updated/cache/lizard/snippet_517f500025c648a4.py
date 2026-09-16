def _cleanup_workflow(config, task_id, args, **kwargs):
    from lightflow.models import Workflow
    if isinstance(args[0], Workflow):
        if config.celery['result_expires'] == 0:
            AsyncResult(task_id).forget()