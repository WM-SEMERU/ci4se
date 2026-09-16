def perform_task(self, service, task_name, account, payload, callback=None):
    data = {'service': service, 'action': task_name, 'account': account}
    data.update(payload)
    response = self._perform_post_request(self.submit_endpoint, data, self.
        token_header)
    task = Task(uuid=response['task_id'], callback=callback)
    self._pending_tasks[task.uuid] = task
    return task