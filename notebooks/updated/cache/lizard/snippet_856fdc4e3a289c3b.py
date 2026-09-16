def update_tasks(self):
    for task in self.task_manager.timeout_tasks():
        self.task_manager.task_done(task.id, TimeoutError('Task timeout',
            task.timeout))
        self.worker_manager.stop_worker(task.worker_id)
    for task in self.task_manager.cancelled_tasks():
        self.task_manager.task_done(task.id, CancelledError())
        self.worker_manager.stop_worker(task.worker_id)