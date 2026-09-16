def and_filter(self, filter_or_string, *args, **kwargs):
    and_filter = self.find_filter(And)
    if and_filter is None:
        and_filter = And()
        self.filters.append(and_filter)
    and_filter.add_filter(build_filter(filter_or_string, *args, **kwargs))
    return and_filter