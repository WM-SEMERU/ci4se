def derivative(self, name, new, max_value=0, time_delta=True, interval=None,
    allow_negative=False, instance=None):
    path = self.get_metric_path(name, instance=instance)
    if path in self.last_values:
        old = self.last_values[path]
        if new < old:
            old = old - max_value
        derivative_x = new - old
        if interval is None:
            interval = float(self.config['interval'])
        if time_delta:
            derivative_y = interval
        else:
            derivative_y = 1
        result = float(derivative_x) / float(derivative_y)
        if result < 0 and not allow_negative:
            result = 0
    else:
        result = 0
    self.last_values[path] = new
    return result