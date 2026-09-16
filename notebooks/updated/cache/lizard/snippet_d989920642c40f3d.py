def _priority_range(policy=None):
    if policy is None:
        policy = libc.sched_getscheduler(0)
        if policy < 0:
            raise OSError(get_errno(), 'sched_getscheduler')
    max = libc.sched_get_priority_max(policy)
    if max < 0:
        raise OSError(get_errno(), 'sched_get_priority_max')
    min = libc.sched_get_priority_min(policy)
    if min < 0:
        raise OSError(get_errno(), 'sched_get_priority_min')
    return min, max