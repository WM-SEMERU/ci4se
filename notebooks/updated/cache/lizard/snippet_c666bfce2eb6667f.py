def can_handle_suffix(self, suffix):
    try:
        return self.remove_prefix(suffix) in self.handled_suffixes
    except IndexError:
        return False