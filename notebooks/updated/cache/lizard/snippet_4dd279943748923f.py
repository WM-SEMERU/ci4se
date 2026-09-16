def update_frame(self, key, ranges=None, plot=None):
    element = self._get_frame(key)
    self._get_title_div(key, '12pt')
    previous_id = self.handles.get('previous_id', None)
    current_id = element._plot_id
    self.handles['previous_id'] = current_id
    self.static_source = self.dynamic and current_id == previous_id
    if (element is None or not self.dynamic and self.static or self.
        streaming and self.streaming[0].data is self.current_frame.data and
        not self.streaming[0]._triggering or self.static_source):
        return
    source = self.handles['source']
    style = self.lookup_options(element, 'style')[self.cyclic_index]
    data, _, style = self.get_data(element, ranges, style)
    columns = self._get_columns(element, data)
    self.handles['table'].columns = columns
    self._update_datasource(source, data)