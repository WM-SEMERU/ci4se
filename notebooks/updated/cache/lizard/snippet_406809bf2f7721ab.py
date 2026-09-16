def get_breaks_lno(self, filename):
    return list(filter(lambda x: x is not None, [getattr(breakpoint, 'line',
        None) for breakpoint in self.breakpoints if breakpoint.on_file(
        filename)]))