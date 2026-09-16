def update(self, workspace, params={}, **options):
    path = '/workspaces/%s' % workspace
    return self.client.put(path, params, **options)