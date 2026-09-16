def write_to(self, group, append=False):
    write_index(self, group, append)
    self._entries['items'].write_to(group)
    self._entries['features'].write_to(group, append)
    self._entries['labels'].write_to(group)
    if self.has_properties():
        self._entries['properties'].write_to(group, append=append)