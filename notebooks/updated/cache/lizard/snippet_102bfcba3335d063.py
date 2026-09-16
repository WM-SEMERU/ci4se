def compress_ranges_to_lists(self):
    clist = []
    for elem in self:
        if isinstance(elem, FixedListSubset):
            clist.append(elem.compress_ranges_to_lists())
        else:
            clist.append(elem)
    return clist