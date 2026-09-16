def restore_prefix(self):
    for removal in self.removals:
        self.current_word = removal.get_subject()
        break
    for removal in self.removals:
        if removal.get_affix_type() == 'DP':
            self.removals.remove(removal)