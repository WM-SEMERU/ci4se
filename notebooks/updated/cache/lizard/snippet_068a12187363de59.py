def unfinished_items(self):
    return [(key, stat) for key, stat in self._statuses.items() if stat not in
        self.DONE_STATES]