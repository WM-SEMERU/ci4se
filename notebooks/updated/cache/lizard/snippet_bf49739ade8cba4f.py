def _get_queue_for_the_action(self, action):
    mod = getattr(action, 'module_type', 'fork')
    queues = list(self.q_by_mod[mod].items())
    if not queues:
        return 0, None
    self.rr_qid = (self.rr_qid + 1) % len(queues)
    worker_id, queue = queues[self.rr_qid]
    return worker_id, queue