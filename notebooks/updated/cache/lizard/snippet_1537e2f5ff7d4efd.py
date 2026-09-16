def add_context(self, name, indices, level=None):
    self._validate_context((name, indices))
    if level is None:
        level = len(self.contexts_ranked)
    self.contexts_ranked.insert(level, name)
    self.contexts[name] = indices