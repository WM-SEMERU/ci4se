def get_effective_tags(self):
    tags = self.patroni.tags.copy()
    if self._disable_sync > 0:
        tags['nosync'] = True
    return tags