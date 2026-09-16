def _viewdata_to_view(self, p_data):
    sorter = Sorter(p_data['sortexpr'], p_data['groupexpr'])
    filters = []
    if not p_data['show_all']:
        filters.append(DependencyFilter(self.todolist))
        filters.append(RelevanceFilter())
        filters.append(HiddenTagFilter())
    filters += get_filter_list(p_data['filterexpr'].split())
    return UIView(sorter, filters, self.todolist, p_data)