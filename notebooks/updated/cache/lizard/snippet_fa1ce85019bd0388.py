def get_queue_stats(self):
    states = QUEUED, ACTIVE, SCHEDULED, ERROR
    pipeline = self.connection.pipeline()
    for state in states:
        pipeline.smembers(self._key(state))
    queue_results = pipeline.execute()
    pipeline = self.connection.pipeline()
    for state, result in zip(states, queue_results):
        for queue in result:
            pipeline.zcard(self._key(state, queue))
    card_results = pipeline.execute()
    queue_stats = defaultdict(dict)
    for state, result in zip(states, queue_results):
        for queue in result:
            queue_stats[queue][state] = card_results.pop(0)
    return queue_stats