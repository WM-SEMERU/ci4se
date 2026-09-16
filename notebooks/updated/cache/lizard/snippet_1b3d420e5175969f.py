def parse_expvar_data(self, data, tags, metrics, max_metrics, namespace):
    count = 0
    for metric in metrics:
        path = metric.get(PATH)
        metric_type = metric.get(TYPE, DEFAULT_TYPE)
        metric_tags = list(metric.get(TAGS, []))
        metric_tags += tags
        alias = metric.get(ALIAS)
        if not path:
            self.warning('Metric %s has no path' % metric)
            continue
        if metric_type not in SUPPORTED_TYPES:
            self.warning('Metric type %s not supported for this check' %
                metric_type)
            continue
        keys = path.split('/')
        values = self.deep_get(data, keys)
        if len(values) == 0:
            self.warning('No results matching path %s' % path)
            continue
        tag_by_path = alias is not None
        for traversed_path, value in values:
            actual_path = '.'.join(traversed_path)
            path_tag = ['path:%s' % actual_path] if tag_by_path else []
            metric_name = alias or self.normalize(actual_path, namespace,
                fix_case=True)
            try:
                float(value)
            except ValueError:
                self.log.warning('Unreportable value for path %s: %s' % (
                    path, value))
                continue
            if count >= max_metrics:
                self.warning(
                    'Reporting more metrics than the allowed maximum. Please contact support@datadoghq.com for more information.'
                    )
                return
            SUPPORTED_TYPES[metric_type](self, metric_name, value, 
                metric_tags + path_tag)
            count += 1