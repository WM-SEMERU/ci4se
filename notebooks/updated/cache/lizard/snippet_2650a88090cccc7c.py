def _expand_containing_using_transitivity(self, containing_contigs):
    for name in containing_contigs:
        containing_contigs[name] = self._get_all_containing(containing_contigs,
            name)
    return containing_contigs