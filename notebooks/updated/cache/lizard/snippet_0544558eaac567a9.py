def visit_Set(self, pattern):
    if len(pattern.elts) > MAX_UNORDERED_LENGTH:
        raise DamnTooLongPattern('Pattern for Set is too long')
    return isinstance(self.node, Set) and any(self.check_list(self.node.
        elts, pattern_elts) for pattern_elts in permutations(pattern.elts))