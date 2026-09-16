def update(self, properties=None):
    if properties is None:
        try:
            self.update_view_data(properties=list(self._cache.keys()))
        except AttributeError:
            pass
    else:
        self.update_view_data(properties=properties)