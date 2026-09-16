def show_tabulated(self, begin, middle, end):
    internal_assert(len(begin) < info_tabulation, 'info message too long',
        begin)
    self.show(begin + ' ' * (info_tabulation - len(begin)) + middle + ' ' + end
        )