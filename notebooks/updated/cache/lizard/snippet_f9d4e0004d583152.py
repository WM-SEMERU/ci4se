def comments(self, limit=None):
    return self._reddit.comments(self.display_name, limit=limit)