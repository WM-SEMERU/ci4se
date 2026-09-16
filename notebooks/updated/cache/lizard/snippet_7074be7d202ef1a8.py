def _get_replication_metrics(self, key, db):
    metrics = self.replication_metrics.get(key)
    if self._is_10_or_above(key, db) and metrics is None:
        self.replication_metrics[key] = dict(self.REPLICATION_METRICS_10)
        metrics = self.replication_metrics.get(key)
    elif self._is_9_1_or_above(key, db) and metrics is None:
        self.replication_metrics[key] = dict(self.REPLICATION_METRICS_9_1)
        if self._is_9_2_or_above(key, db):
            self.replication_metrics[key].update(self.REPLICATION_METRICS_9_2)
        metrics = self.replication_metrics.get(key)
    return metrics