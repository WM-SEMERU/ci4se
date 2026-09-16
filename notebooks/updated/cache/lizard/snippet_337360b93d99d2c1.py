def _get_subcats(self, recurse=False):
    if recurse:
        return sorted([Category(e) for e in self._subcats_recursive], key=
            lambda c: c.sort_breadcrumb)
    parts = len(self.path.split('/')) + 1 if self.path else 1
    subcats = [c.split('/')[:parts] for c in self._subcats_recursive]
    subcats = {'/'.join(c) for c in subcats}
    return sorted([Category(c) for c in subcats], key=lambda c: c.sort_name or
        c.name)