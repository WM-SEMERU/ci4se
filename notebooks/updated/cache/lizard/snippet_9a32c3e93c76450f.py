def remove_filter(self, filter_attr):
    filter_attr = self._get_mapping(filter_attr)
    new_filters = []
    remove_chain = False
    for flt in self._filters:
        if isinstance(flt, tuple):
            if flt[0] == filter_attr:
                remove_chain = True
            else:
                new_filters.append(flt)
        elif remove_chain is False:
            new_filters.append(flt)
        else:
            remove_chain = False
    self._filters = new_filters