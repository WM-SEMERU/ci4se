def get_app_guid(self, app_name):
    summary = self.space.get_space_summary()
    for app in summary['apps']:
        if app['name'] == app_name:
            return app['guid']