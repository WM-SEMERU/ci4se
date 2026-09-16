def delete(self, project_status, params={}, **options):
    path = '/project_statuses/%s' % project_status
    return self.client.delete(path, params, **options)