def macro2micro(self, macro_indices):

    def from_partition(partition, macro_indices):
        micro_indices = itertools.chain.from_iterable(partition[i] for i in
            macro_indices)
        return tuple(sorted(micro_indices))
    if self.blackbox and self.coarse_grain:
        cg_micro_indices = from_partition(self.coarse_grain.partition,
            macro_indices)
        return from_partition(self.blackbox.partition, reindex(
            cg_micro_indices))
    elif self.blackbox:
        return from_partition(self.blackbox.partition, macro_indices)
    elif self.coarse_grain:
        return from_partition(self.coarse_grain.partition, macro_indices)
    return macro_indices