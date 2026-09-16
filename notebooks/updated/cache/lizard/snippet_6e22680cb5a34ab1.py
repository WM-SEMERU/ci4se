def get(self, task_id=None, params=None):
    return self.transport.perform_request('GET', _make_path('_tasks',
        task_id), params=params)