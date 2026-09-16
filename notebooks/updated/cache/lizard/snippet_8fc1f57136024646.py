def expand_branch_name(self, name):
    if not name:
        return self.default_revision
    branches = list(self.find_branches_raw())
    for prefix, other_name, revision_id in branches:
        if prefix == 'refs/heads/' and name == other_name:
            logger.debug('Branch name %r matches local branch.', name)
            return name
    for prefix, other_name, revision_id in branches:
        if prefix.startswith('refs/remotes/') and name == other_name:
            unambiguous_name = prefix + name
            logger.debug('Branch name %r matches remote branch %r.', name,
                unambiguous_name)
            return unambiguous_name
    logger.debug('Failed to expand branch name %r.', name)
    return name