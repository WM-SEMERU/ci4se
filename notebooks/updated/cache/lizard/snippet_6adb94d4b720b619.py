def _get_columns(self):
    return [self] + [c for c in self.children if isinstance(c, TreeViewColumn)]