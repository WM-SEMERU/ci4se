def reset(self):
    [(a().remove_observer(self, self.on_cache_changed) if a() is not None else
        None) for [a, _] in self.cached_input_ids.values()]
    self.order = collections.deque()
    self.cached_inputs = {}
    self.cached_input_ids = {}
    self.cached_outputs = {}
    self.inputs_changed = {}