def __configure_timeline(self, *args):
    size_x, size_y = self._timeline.winfo_reqwidth(
        ), self._timeline.winfo_reqheight()
    self._canvas_scroll.config(scrollregion='0 0 {0} {1}'.format(size_x, 
        size_y - 5))