def _sort(self, short_list, sorts):
    sort_values = self._index_columns(sorts)
    output = []

    def _sort_more(short_list, i, sorts):
        if len(sorts) == 0:
            output.extend(short_list)
        sort = sorts[0]
        index = self._index[sort_values[i]]
        if sort.sort == 1:
            sorted_keys = sorted(index.keys())
        elif sort.sort == -1:
            sorted_keys = reversed(sorted(index.keys()))
        else:
            sorted_keys = list(index.keys())
        for k in sorted_keys:
            self._sort(index[k] & short_list, i + 1, sorts[1:])
    _sort_more(short_list, 0, sorts)
    return output