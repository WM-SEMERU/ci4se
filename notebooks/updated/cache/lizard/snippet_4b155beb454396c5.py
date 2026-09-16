def get_metric_by_name(self, metric_name, **kwargs):
    return self._get_object_by_name(self._METRIC_ENDPOINT_SUFFIX,
        metric_name, **kwargs)