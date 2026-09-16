def add_filter_by_pattern(self, pattern, filter_type=DefaultFilterType):
    self.add_filter(FilterPattern(pattern), filter_type)
    return self