def Get(self, fields=None):
    result = super(_GaugeMetric, self).Get(fields=fields)
    if callable(result):
        return result()
    else:
        return result