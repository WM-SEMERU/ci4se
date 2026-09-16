def _schedule_slice(cls, shard_state, tstate, queue_name=None, eta=None,
    countdown=None):
    queue_name = queue_name or os.environ.get('HTTP_X_APPENGINE_QUEUENAME',
        'default')
    task = cls._state_to_task(tstate, shard_state, eta, countdown)
    cls._add_task(task, tstate.mapreduce_spec, queue_name)