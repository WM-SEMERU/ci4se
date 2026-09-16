def has_parent(self, term):
    for parent in self.parents:
        if parent.item_id == term or parent.has_parent(term):
            return True
    return False