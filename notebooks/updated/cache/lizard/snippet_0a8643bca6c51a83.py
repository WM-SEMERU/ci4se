def has_local_as(self, local_as, max_count=0):
    _count = 0
    for as_path_seg in self.value:
        _count += list(as_path_seg).count(local_as)
    return _count > max_count