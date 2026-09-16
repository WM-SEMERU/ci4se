def move(self, group, index=None):
    return self.group.db.move_entry(self, group, index=index)