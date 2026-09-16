def query_metric_definition(self, metric_type, metric_id):
    return self._get(self._get_metrics_single_url(metric_type, metric_id))