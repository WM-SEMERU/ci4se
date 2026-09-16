def taskotron_task_particular_or_changed_outcome(config, message, outcome=
    'FAILED,NEEDS_INSPECTION'):
    return taskotron_task_outcome(config, message, outcome
        ) or taskotron_changed_outcome(config, message)