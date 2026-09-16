def _normalize(self, metric_name, submit_method, prefix):
    metric_prefix = 'mongodb.' if not prefix else 'mongodb.{0}.'.format(prefix)
    metric_suffix = 'ps' if submit_method == RATE else ''
    for pattern, repl in iteritems(self.CASE_SENSITIVE_METRIC_NAME_SUFFIXES):
        metric_name = re.compile(pattern).sub(repl, metric_name)
    return '{metric_prefix}{normalized_metric_name}{metric_suffix}'.format(
        normalized_metric_name=self.normalize(metric_name.lower()),
        metric_prefix=metric_prefix, metric_suffix=metric_suffix)