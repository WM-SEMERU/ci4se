def hot(self, limit=None):
    return self._reddit.hot(self.display_name, limit=limit)