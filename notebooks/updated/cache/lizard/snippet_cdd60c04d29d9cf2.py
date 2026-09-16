def can(self, event):
    return [t.new_state for t in self._transitions if t.event.equals(event)]