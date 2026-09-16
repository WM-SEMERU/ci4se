def fetch_all_backups(self):
    r
    api = self.doapi_manager
    for obj in api.paginate(self.url + '/backups', 'backups'):
        yield Image(obj, doapi_manager=api)