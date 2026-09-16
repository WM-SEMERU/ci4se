def _get_all_containing(self, containing_contigs, name, exclude=None,
    max_depth=10):
    contains_name = set()
    if max_depth < 0:
        return contains_name
    if name in containing_contigs:
        for containing_contig in containing_contigs[name]:
            if containing_contig == exclude:
                continue
            contains_name.add(containing_contig)
            new_names = self._get_all_containing(containing_contigs,
                containing_contig, exclude=name, max_depth=max_depth - 1)
            new_names.discard(name)
            contains_name.update(new_names)
    return contains_name