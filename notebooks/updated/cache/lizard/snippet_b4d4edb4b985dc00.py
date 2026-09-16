def sort_values(self, by, ascending=True):
    check_type(ascending, bool)
    check_str_or_list_str(by)
    by = as_list(by)
    if len(by) > 1:
        raise NotImplementedError(
            'Weld does not yet support sorting on multiple columns')
    all_data = self.reset_index()
    by_data = all_data[by]
    sorted_indices = weld_sort(by_data._gather_data_for_weld(), by_data.
        _gather_weld_types(), 'sort_index', ascending=ascending)
    new_index = self.index._iloc_indices(sorted_indices)
    new_columns = list(self._iter())
    new_column_names = [column.name for column in new_columns]
    new_columns = [_series_iloc(column, sorted_indices, new_index) for
        column in new_columns]
    new_data = OrderedDict(zip(new_column_names, new_columns))
    return DataFrame(new_data, new_index)