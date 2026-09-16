def display(self):
    if self.is_undoc_member and 'undoc-members' not in self.options:
        return False
    if self.is_private_member and 'private-members' not in self.options:
        return False
    if self.is_special_member and 'special-members' not in self.options:
        return False
    return True