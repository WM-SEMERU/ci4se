def add_metric(self, metric_name, measurable, config=None):
    metric = KafkaMetric(metric_name, measurable, config or self.config)
    self.register_metric(metric)