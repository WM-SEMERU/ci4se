def add_subtask(self, task, params={}, **options):
    path = '/tasks/%s/subtasks' % task
    return self.client.post(path, params, **options)