def get_views(self, name=None):
    return self._get_elements(self.views, 'views', View, name=name)