def get_totals(self):
    total_added = 0
    total_removed = 0
    patch = PatchSet(self.diff)
    total_added += sum([edit.added for edit in patch])
    total_removed += sum([edit.removed for edit in patch])
    return {self.ADD: total_added, self.DEL: total_removed}