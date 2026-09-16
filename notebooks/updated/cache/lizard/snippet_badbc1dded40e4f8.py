def top(self, limit=None):
    return self._reddit.top(self.display_name, limit=limit)