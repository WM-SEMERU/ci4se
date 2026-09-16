def targets_by_file(self, targets):
    targets_by_file = defaultdict(OrderedSet)
    for target in targets:
        for f in self.files_for_target(target):
            targets_by_file[f].add(target)
    return targets_by_file