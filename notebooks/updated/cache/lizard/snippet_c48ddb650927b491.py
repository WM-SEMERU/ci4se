def _get_archiver_metrics(self, key, db):
    metrics = self.archiver_metrics.get(key)
    if self._is_9_4_or_above(key, db) and metrics is None:
        sub_key = key[:2]
        if sub_key in self.db_archiver_metrics:
            self.archiver_metrics[key] = None
            self.log.debug(
                'Not collecting archiver metrics for key: {0} as they are already collected by another instance'
                .format(key))
            return None
        self.db_archiver_metrics.append(sub_key)
        self.archiver_metrics[key] = dict(self.COMMON_ARCHIVER_METRICS)
        metrics = self.archiver_metrics.get(key)
    if not metrics:
        return None
    return {'descriptors': [], 'metrics': metrics, 'query':
        'select %s FROM pg_stat_archiver', 'relation': False}