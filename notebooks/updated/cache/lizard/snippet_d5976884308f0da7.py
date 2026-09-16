def on_unicode_checkbox(self, w=None, state=False):
    logging.debug('unicode State is %s', state)
    self.controller.smooth_graph_mode = state
    if state:
        self.hline = urwid.AttrWrap(urwid.SolidFill('▂'), 'line')
    else:
        self.hline = urwid.AttrWrap(urwid.SolidFill(' '), 'line')
    for graph in self.graphs.values():
        graph.set_smooth_colors(state)
    self.show_graphs()