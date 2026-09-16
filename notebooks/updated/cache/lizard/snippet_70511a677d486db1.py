def get_settings(self, index):
    settings = self.es.indices.get_settings(index=index)
    return next(iter(settings.values()))