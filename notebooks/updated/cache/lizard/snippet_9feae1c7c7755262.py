def _check_request(self):
    todo = []
    for task in self._postpone_request:
        if task['project'] not in self.projects:
            continue
        if self.projects[task['project']].task_queue.is_processing(task[
            'taskid']):
            todo.append(task)
        else:
            self.on_request(task)
    self._postpone_request = todo
    tasks = {}
    while len(tasks) < self.LOOP_LIMIT:
        try:
            task = self.newtask_queue.get_nowait()
        except Queue.Empty:
            break
        if isinstance(task, list):
            _tasks = task
        else:
            _tasks = task,
        for task in _tasks:
            if not self.task_verify(task):
                continue
            if task['taskid'] in self.projects[task['project']].task_queue:
                if not task.get('schedule', {}).get('force_update', False):
                    logger.debug(
                        'ignore newtask %(project)s:%(taskid)s %(url)s', task)
                    continue
            if task['taskid'] in tasks:
                if not task.get('schedule', {}).get('force_update', False):
                    continue
            tasks[task['taskid']] = task
    for task in itervalues(tasks):
        self.on_request(task)
    return len(tasks)