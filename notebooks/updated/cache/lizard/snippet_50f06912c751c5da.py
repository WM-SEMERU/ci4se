def _add_single_metric(self, timestamp, metric_name, value):
    self._data['timestamp'].append(timestamp)
    self._data['metric_name'].append(metric_name)
    self._data['value'].append(value)