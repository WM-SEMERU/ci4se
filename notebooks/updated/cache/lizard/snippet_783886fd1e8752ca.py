def get_waiting_keys(cls, names):
    return [queue.waiting.key for queue in cls.get_all_by_priority(names)]