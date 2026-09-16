def start_log_task(task, logger=logging, level='info'):
    getattr(logger, level)(START_TASK_TRIGGER_MSG % task)