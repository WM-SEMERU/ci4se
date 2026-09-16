def current_revision(self):
    if self.current_index is None:
        return None
    if len(self.revisions) > self.current_index:
        return self.revisions[self.current_index]
    return None