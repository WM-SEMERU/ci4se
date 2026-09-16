def _get_queue_name(cls, queue_name=None):
    if queue_name is None and cls.queue_name is None:
        raise LimpydJobsException("Queue's name not defined")
    if queue_name is None:
        return cls.queue_name
    return queue_name