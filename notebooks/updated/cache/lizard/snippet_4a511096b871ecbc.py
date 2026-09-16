def restricted_registry(self, names):
    names = set(names)
    collectors = set()
    with self._lock:
        for name in names:
            if name in self._names_to_collectors:
                collectors.add(self._names_to_collectors[name])
    metrics = []
    for collector in collectors:
        for metric in collector.collect():
            samples = [s for s in metric.samples if s[0] in names]
            if samples:
                m = Metric(metric.name, metric.documentation, metric.type)
                m.samples = samples
                metrics.append(m)


    class RestrictedRegistry(object):

        def collect(self):
            return metrics
    return RestrictedRegistry()