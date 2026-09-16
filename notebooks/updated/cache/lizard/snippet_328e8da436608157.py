def task_add(self, description, tags=None, **kw):
    task = self._stub_task(description, tags, **kw)
    task['status'] = Status.PENDING
    if not 'entry' in task:
        task['entry'] = str(int(time.time()))
    if not 'uuid' in task:
        task['uuid'] = str(uuid.uuid4())
    id = self._task_add(task, Status.PENDING)
    task['id'] = id
    return task