def check_num_tasks(chain, task_count):
    errors = []
    min_decision_tasks = 1
    if task_count['decision'] < min_decision_tasks:
        errors.append('{} decision tasks; we must have at least {}!'.format
            (task_count['decision'], min_decision_tasks))
    raise_on_errors(errors)