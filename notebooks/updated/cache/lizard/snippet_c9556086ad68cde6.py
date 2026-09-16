def is_supergroup(self, subgroup):
    warnings.warn(
        'This is not fully functional. Only trivial subsets are tested right now. '
        )
    return set(subgroup.symmetry_ops).issubset(self.symmetry_ops)