def update(self):
    if self._owner_changed:
        self.update_owner(self.owner)
    self._resources = [res.name for res in self.resources]
    return self.parent.update(self)