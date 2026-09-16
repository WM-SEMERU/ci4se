def queue(self, *args, **kwargs):
    queue_name = kwargs.pop('queue', self.queue_name)
    timeout = kwargs.pop('timeout', self.timeout)
    result_ttl = kwargs.pop('result_ttl', self.result_ttl)
    ttl = kwargs.pop('ttl', self.ttl)
    depends_on = kwargs.pop('depends_on', self._depends_on)
    job_id = kwargs.pop('job_id', None)
    at_front = kwargs.pop('at_front', self._at_front)
    meta = kwargs.pop('meta', self._meta)
    description = kwargs.pop('description', self._description)
    return self.rq.get_queue(queue_name).enqueue_call(self.wrapped, args=
        args, kwargs=kwargs, timeout=timeout, result_ttl=result_ttl, ttl=
        ttl, depends_on=depends_on, job_id=job_id, at_front=at_front, meta=
        meta, description=description)