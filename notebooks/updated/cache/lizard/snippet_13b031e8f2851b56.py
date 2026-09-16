def _estimate_free(self):
    capacity_deferred = self.channel.total_capacity()
    open_tasks_deferred = self.channel.tasks(state=[task_states.OPEN])
    avg_delta_deferred = self.estimate_duration()
    deferreds = [capacity_deferred, open_tasks_deferred, avg_delta_deferred]
    results = yield defer.gatherResults(deferreds, consumeErrors=True)
    capacity, open_tasks, avg_delta = results
    open_weight = sum([task.weight for task in open_tasks])
    if open_weight >= capacity:
        raise NotImplementedError('channel %d is at capacity' % self.channel_id
            )
    start_time = self.created + SLEEPTIME
    if avg_delta is None:
        defer.returnValue(None)
    est_completion = start_time + avg_delta
    defer.returnValue(est_completion)