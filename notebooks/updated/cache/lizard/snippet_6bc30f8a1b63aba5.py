def tasks(self, project, params={}, **options):
    path = '/projects/%s/tasks' % project
    return self.client.get_collection(path, params, **options)