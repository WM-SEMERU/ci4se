def get_tasks_with_tag(self, tag, params={}, **options):
    path = '/tags/%s/tasks' % tag
    return self.client.get_collection(path, params, **options)