def _topological_sort(self, targets):
    target_set = set(targets)
    return [t for t in reversed(sort_targets(targets)) if t in target_set]