def _init_plot_handles(self):
    plots = [self.plot]
    if self.plot.subplots:
        plots += list(self.plot.subplots.values())
    handles = {}
    for plot in plots:
        for k, v in plot.handles.items():
            handles[k] = v
    self.plot_handles = handles
    requested = {}
    for h in (self.models + self.extra_models):
        if h in self.plot_handles:
            requested[h] = handles[h]
        elif h in self.extra_models:
            print(
                'Warning %s could not find the %s model. The corresponding stream may not work.'
                 % (type(self).__name__, h))
    self.handle_ids.update(self._get_stream_handle_ids(requested))
    return requested