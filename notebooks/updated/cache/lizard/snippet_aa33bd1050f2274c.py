def _branch_descendants(self, branch=None):
    branch = branch or self.branch
    for parent, (child, _, _, _, _) in self._branches.items():
        if parent == branch:
            yield child