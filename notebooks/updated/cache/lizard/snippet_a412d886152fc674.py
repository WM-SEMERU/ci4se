def workload_state_compare(current_workload_state, workload_state):
    hierarchy = {'unknown': -1, 'active': 0, 'maintenance': 1, 'waiting': 2,
        'blocked': 3}
    if hierarchy.get(workload_state) is None:
        workload_state = 'unknown'
    if hierarchy.get(current_workload_state) is None:
        current_workload_state = 'unknown'
    if hierarchy.get(current_workload_state) > hierarchy.get(workload_state):
        return current_workload_state
    else:
        return workload_state