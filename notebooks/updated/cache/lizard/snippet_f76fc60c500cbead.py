def set_interval(self, interval=None, change_status=True, force_update=False):
    if interval is None:
        interval = self._interval
    interval = self._restrict_interval(interval)
    if not force_update and interval == self._interval:
        return
    self._interval = interval
    start, end = interval
    self.clear()
    if change_status:
        self.set_status('Interval: {:.3f} s - {:.3f} s'.format(start, end))
    traces = self.traces(interval)
    ymin, ymax = traces.data.min(), traces.data.max()
    data_bounds = start, ymin, end, ymax
    self._data_bounds = data_bounds
    self._waveform_times = []
    self._plot_traces(traces.data, color=traces.get('color', None),
        data_bounds=data_bounds)
    waveforms = traces.waveforms
    assert isinstance(waveforms, list)
    for w in waveforms:
        self._plot_waveforms(waveforms=w.data, color=w.color, channel_ids=w
            .get('channel_ids', None), start_time=w.start_time, data_bounds
            =data_bounds)
        self._waveform_times.append((w.start_time, w.spike_id, w.
            spike_cluster, w.get('channel_ids', None)))
    if self.do_show_labels:
        self._plot_labels(traces.data, data_bounds=data_bounds)
    self.build()
    self.update()