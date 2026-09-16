def push(self, metric_type, metric_id, value, timestamp=None):
    if type(timestamp) is datetime:
        timestamp = datetime_to_time_millis(timestamp)
    item = create_metric(metric_type, metric_id, create_datapoint(value,
        timestamp))
    self.put(item)