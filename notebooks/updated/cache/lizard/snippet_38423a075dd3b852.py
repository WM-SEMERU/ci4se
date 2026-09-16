def _rebuild_entries(self):
    self.entries = []

    def collapse_entries(group):
        for entry in group.entries:
            self.entries.append(entry)
        for subgroup in group.children:
            collapse_entries(subgroup)
    collapse_entries(self.root)